# Generated by Django 3.2.15 on 2023-01-04 12:36

from django.db import migrations

from ..hydrators import dehydrate_value

settings = [
    {
        "setting": "enable_oauth2_client",
        "python_type": "bool",
        "dry_value": False,
        "is_public": True,
    },
    {"setting": "oauth2_provider", "is_public": True},
    {"setting": "oauth2_client_id", "is_public": False},
    {"setting": "oauth2_client_secret", "is_public": False},
    {"setting": "oauth2_scopes", "is_public": False},
    {"setting": "oauth2_login_url", "is_public": False},
    {"setting": "oauth2_token_url", "is_public": False},
    {"setting": "oauth2_token_method", "dry_value": "POST", "is_public": False},
    {"setting": "oauth2_token_extra_headers", "is_public": False},
    {
        "setting": "oauth2_json_token_path",
        "dry_value": "access_token",
        "is_public": False,
    },
    {"setting": "oauth2_user_url", "is_public": False},
    {"setting": "oauth2_user_method", "dry_value": "GET", "is_public": False},
    {
        "setting": "oauth2_user_token_location",
        "dry_value": "QUERY",
        "is_public": False,
    },
    {
        "setting": "oauth2_user_token_name",
        "dry_value": "access_token",
        "is_public": False,
    },
    {"setting": "oauth2_user_extra_headers", "is_public": False},
    {
        "setting": "oauth2_send_welcome_email",
        "python_type": "bool",
        "dry_value": False,
        "is_public": False,
    },
    {"setting": "oauth2_json_id_path", "dry_value": "id", "is_public": False},
    {"setting": "oauth2_json_name_path", "dry_value": "name", "is_public": False},
    {"setting": "oauth2_json_email_path", "dry_value": "email", "is_public": False},
    {"setting": "oauth2_json_avatar_path", "is_public": False},
]


def create_settings(apps, _):
    Setting = apps.get_model("misago_conf", "Setting")
    for setting in settings:
        data = setting.copy()
        if "python_type" in data and "dry_value" in data:
            data["dry_value"] = dehydrate_value(data["python_type"], data["dry_value"])

        Setting.objects.create(**setting)


class Migration(migrations.Migration):
    dependencies = [
        ("misago_conf", "0006_add_index_message"),
    ]

    operations = [migrations.RunPython(create_settings)]
