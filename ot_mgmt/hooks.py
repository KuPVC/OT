from . import __version__ as app_version

app_name = "ot_mgmt"
app_title = "OT Mgmt"
app_publisher = "Dx"
app_description = "OT Mgmt"
app_email = "dx"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/ot_mgmt/css/ot_mgmt.css"
# app_include_js = "/assets/ot_mgmt/js/ot_mgmt.js"

# include js, css files in header of web template
# web_include_css = "/assets/ot_mgmt/css/ot_mgmt.css"
# web_include_js = "/assets/ot_mgmt/js/ot_mgmt.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "ot_mgmt/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

fixtures = [
    {
        "dt":"Custom Field",
        "filters":[["module","=","OT Mgmt"]]
    },
    {
        "dt":"Property Setter",
        "filters":[["module","=","OT Mgmt"]]
    },
    {
        "dt":"Report",
        "filters":[["name","in",["Overtime Summary"]]]
    }
]

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "ot_mgmt.utils.jinja_methods",
#	"filters": "ot_mgmt.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "ot_mgmt.install.before_install"
# after_install = "ot_mgmt.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "ot_mgmt.uninstall.before_uninstall"
# after_uninstall = "ot_mgmt.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ot_mgmt.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Attendance": {
		"on_submit":"ot_mgmt.ot_mgmt.ot_mgmt.att_on_submit"
	},
	"Salary Slip": {
		"before_validate":"ot_mgmt.ot_mgmt.ot_mgmt.salary_slip_validate"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"ot_mgmt.tasks.all"
#	],
#	"daily": [
#		"ot_mgmt.tasks.daily"
#	],
#	"hourly": [
#		"ot_mgmt.tasks.hourly"
#	],
#	"weekly": [
#		"ot_mgmt.tasks.weekly"
#	],
#	"monthly": [
#		"ot_mgmt.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "ot_mgmt.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "ot_mgmt.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "ot_mgmt.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["ot_mgmt.utils.before_request"]
# after_request = ["ot_mgmt.utils.after_request"]

# Job Events
# ----------
# before_job = ["ot_mgmt.utils.before_job"]
# after_job = ["ot_mgmt.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"ot_mgmt.auth.validate"
# ]
