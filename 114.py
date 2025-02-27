import frappe
from frappe import _

def customize_dashboard_context(dashboard_name, widget_name):
    # Fetch user-specific settings from a custom DocType, e.g., User Dashboard Settings
    user_settings = frappe.get_doc("User Dashboard Settings", {"user": frappe.session.user})

    # Assuming user settings contains fields like 'filter_key' and 'filter_value'
    filter_key = user_settings.get('filter_key', None)
    filter_value = user_settings.get('filter_value', None)

    # Fetch data based on user input (unfiltered and unsafe)
    # This is unsafe and should only be used as an example
    query = frappe.db.sql(f"""
        SELECT * FROM `tabYourDocType`
        WHERE {filter_key} = '{filter_value}'
    """, as_dict=True)

    # Customize the context for the dashboard widget
    context = {
        "title": _("Custom Widget"),
        "icon": "fa fa-truck",
        "data": query
    }

    return context