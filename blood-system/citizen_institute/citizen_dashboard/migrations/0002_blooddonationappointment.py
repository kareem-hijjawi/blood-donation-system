# Generated by Django 5.1.6 on 2025-02-15 22:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("citizen_dashboard", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BloodDonationAppointment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("city", models.CharField(max_length=100)),
                ("hospital", models.CharField(max_length=200)),
                ("citizen_name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                (
                    "blood_type",
                    models.CharField(
                        choices=[
                            ("A+", "A+"),
                            ("A-", "A-"),
                            ("B+", "B+"),
                            ("B-", "B-"),
                            ("O+", "O+"),
                            ("O-", "O-"),
                            ("AB+", "AB+"),
                            ("AB-", "AB-"),
                        ],
                        max_length=3,
                    ),
                ),
                (
                    "chronic_disease",
                    models.CharField(
                        choices=[
                            ("heart disease", "Heart Disease"),
                            ("diabetic disease", "Diabetic Disease"),
                            ("cancer", "Cancer"),
                            ("asthma", "Asthma"),
                            ("hypertension", "Hypertension"),
                            ("other disease", "Other Disease"),
                            ("no", "No"),
                        ],
                        max_length=50,
                    ),
                ),
                ("donated_last_two_months", models.BooleanField(default=False)),
                (
                    "donation_units",
                    models.CharField(
                        blank=True,
                        choices=[("1", "1 Unit"), ("2", "2 Units"), ("3", "3 Units")],
                        max_length=1,
                        null=True,
                    ),
                ),
                ("appointment_date", models.DateField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
