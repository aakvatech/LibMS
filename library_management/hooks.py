from . import __version__ as app_version

app_name = "library_management"
app_title = "Library Management"
app_publisher = "ramjanali"
app_description = "Library Management System"
app_email = "ramjan@lalnco.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/library_management/css/library_management.css"
# app_include_js = "/assets/library_management/js/library_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/library_management/css/library_management.css"
# web_include_js = "/assets/library_management/js/library_management.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "library_management/public/scss/website"

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
#	"methods": "library_management.utils.jinja_methods",
#	"filters": "library_management.utils.jinja_filters"
# }
jinja = {
    "methods": ["library_management.custom_api.generate_qrcode"]
}

# Installation
# ------------

# before_install = "library_management.install.before_install"
after_install = "library_management.custom_api.create_uom"

# Uninstallation
# ------------

# before_uninstall = "library_management.uninstall.before_uninstall"
# after_uninstall = "library_management.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "library_management.notifications.get_notification_config"

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

# doc_events = {
# 	# "*": {
# 	# 	# "on_update": "method",
# 	# 	# "on_cancel": "method",
# 	# 	# "on_trash": "method",
#     #     "on_submit": "library_management.library_management.library_management.doctype.library_membership.library_membership.check_duplicate_membership"
# 	# },
#     "Library Membership": {
# 		"before_save": "library_management.library_management.doctype.library_membership.library_membership.check_duplicate_membership"
# 	}
# }

# Scheduled Tasks
# ---------------

scheduler_events = {
	"daily": [
        "library_management.library_management.doctype.library_membership.library_membership.auto_expire_memberships"
	]
}

# scheduler_events = {
#	"all": [
#		"library_management.tasks.all"
#	],
#	"daily": [
#		"library_management.tasks.daily"
#	],
#	"hourly": [
#		"library_management.tasks.hourly"
#	],
#	"weekly": [
#		"library_management.tasks.weekly"
#	],
#	"monthly": [
#		"library_management.tasks.monthly"
#	],
# }
# Testing
# -------

# before_tests = "library_management.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "library_management.event.get_events"
# }

override_whitelisted_methods = {
    "library_management.library_management.doctype.book_reservation.book_reservation.count_books_issued": "library_management.custom_api.count_books_issued",
    "book_allowed_issue.allowed_book": "library_management.custom_api.allowed_book",
    "fetch_member_details.fetch_member_issue_book_detail": "library_management.custom_api.fetch_member_issue_book_detail",
    "fetch_member_issue_book_detail": "library_management.library_management.doctype.book_transaction.book_transaction.fetch_member_issue_book_detail",
    "auto_expire_memberships":"library_management.library_management.doctype.library_membership.library_membership.auto_expire_memberships",
    "library_management.custom_api.create_uom":"library_management.custom_api.create_uom"
    #"get_data.check_duplicate_membership": "library_management.library_management.doctype.library_membership.library_membership.check_duplicate_membership"
}


# "book_allowed_issue.allowed_book": "library_management.custom_api.allowed_book"
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "library_management.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]


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
#	"library_management.auth.validate"
# ]
