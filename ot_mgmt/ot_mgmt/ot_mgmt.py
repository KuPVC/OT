import frappe
from frappe.utils import (time_diff_in_hours)
from hrms.hr.utils import get_holiday_dates_for_employee
# Attendance On Submit: Will fetch the shift  details and based on that it'll calculate overtimte and HOT

def att_on_submit(doc,method=None):
    ot = hot = late_hours = 0

    is_holiday = len(get_holiday_dates_for_employee(doc.employee,doc.attendance_date,doc.attendance_date)) > 0

    if not doc.shift or not doc.working_hours:
        return

    (shift_end,shift_start,break_hours,enable_ot,enable_hot,shift_threshold) = frappe.db.get_value('Shift Type',doc.shift,['end_time','start_time','break_hours','enable_ot','enable_hot','shift_threshold'])
    shift_hours = time_diff_in_hours(shift_end,shift_start)

    if shift_threshold < 1:
        shift_threshold = 1

    if doc.working_hours <= shift_threshold:
        break_hours = 0

    if is_holiday and enable_hot:
        hot = doc.working_hours - break_hours
    elif not is_holiday and enable_ot:
        ot = doc.working_hours - shift_hours
        if ot < 0:
            late_hours = - ot
            ot = 0
    doc.db_set('shift_hours',shift_hours)
    doc.db_set('break_hours',break_hours)
    doc.db_set('ot',ot)
    doc.db_set('hot',hot)
    doc.db_set('late_hours',late_hours)


# Salary Slip Before Validate 

def salary_slip_validate(doc,method=None):
    doc.ot,doc.hot,doc.late_hours = frappe.db.sql("""
                                      SELECT
                                        SUM(ot) ot, SUM(hot) hot, SUM(late_hours) late_hours
                                      FROM
                                        `tabAttendance`
                                      WHERE
                                        employee = %s
                                      AND
                                        docstatus = 1
                                      AND
                                        attendance_date BETWEEN %s AND %s
                                      """,(doc.employee,doc.start_date,doc.end_date))[0]