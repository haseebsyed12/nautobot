# Generated by Django 3.2.23 on 2024-02-15 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("dcim", "0054_softwareimage_softwareversion"),
        ("virtualization", "0026_change_virtualmachine_primary_ip_fields"),
    ]

    operations = [
        migrations.AddField(
            model_name="virtualmachine",
            name="software_image_files",
            field=models.ManyToManyField(blank=True, related_name="virtual_machines", to="dcim.SoftwareImageFile"),
        ),
        migrations.AddField(
            model_name="virtualmachine",
            name="software_version",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="virtual_machines",
                to="dcim.softwareversion",
            ),
        ),
    ]