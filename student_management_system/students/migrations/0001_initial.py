# Generated by Django 5.1.7 on 2025-03-17 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('address', models.TextField()),
                ('nationality', models.CharField(max_length=50)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pics/')),
                ('guardian_name', models.CharField(max_length=100)),
                ('guardian_phone', models.CharField(max_length=15)),
                ('guardian_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('guardian_relation', models.CharField(max_length=50)),
                ('admission_date', models.DateField(auto_now_add=True)),
                ('course', models.CharField(max_length=150)),
                ('program_name', models.CharField(choices=[('B.Tech', 'Bachelor of Technology'), ('M.Tech', 'Master of Technology'), ('B.Sc', 'Bachelor of Science'), ('M.Sc', 'Master of Science'), ('B.Com', 'Bachelor of Commerce'), ('M.Com', 'Master of Commerce'), ('B.A', 'Bachelor of Arts'), ('M.A', 'Master of Arts'), ('B.B.A', 'Bachelor of Business Administration'), ('M.B.A', 'Master of Business Administration'), ('B.C.A', 'Bachelor of Computer Applications'), ('M.C.A', 'Master of Computer Applications'), ('B.Ed', 'Bachelor of Education'), ('M.Ed', 'Master of Education'), ('B.Arch', 'Bachelor of Architecture'), ('M.Arch', 'Master of Architecture'), ('B.Pharma', 'Bachelor of Pharmacy'), ('M.Pharma', 'Master of Pharmacy'), ('B.Sc Nursing', 'Bachelor of Science in Nursing'), ('M.Sc Nursing', 'Master of Science in Nursing'), ('BDS', 'Bachelor of Dental Surgery'), ('MDS', 'Master of Dental Surgery'), ('MBBS', 'Bachelor of Medicine and Bachelor of Surgery'), ('MD', 'Doctor of Medicine'), ('MS', 'Master of Surgery'), ('DM', 'Doctorate of Medicine'), ('M.Ch', 'Master of Chirurgiae'), ('Diploma', 'Diploma'), ('PG Diploma', 'Post Graduate Diploma'), ('Ph.D', 'Doctor of Philosophy'), ('M.Phil', 'Master of Philosophy'), ('LLB', 'Bachelor of Laws'), ('LLM', 'Master of Laws'), ('B.Arch', 'Bachelor of Architecture'), ('M.Arch', 'Master of Architecture'), ('B.Pharma', 'Bachelor of Pharmacy'), ('M.Pharma', 'Master of Pharmacy'), ('B.Sc Nursing', 'Bachelor of Science in Nursing'), ('M.Sc Nursing', 'Master of Science in Nursing'), ('BDS', 'Bachelor of Dental Surgery'), ('MDS', 'Master of Dental Surgery'), ('MBBS', 'Bachelor of Medicine and Bachelor of Surgery'), ('MD', 'Doctor of Medicine'), ('MS', 'Master of Surgery'), ('DM', 'Doctorate of Medicine'), ('M.Ch', 'Master of Chirurgiae'), ('Diploma', 'Diploma'), ('PG Diploma', 'Post Graduate Diploma'), ('Ph.D', 'Doctor of Philosophy'), ('M.Phil', 'Master of Philosophy'), ('LLB', 'Bachelor of Laws'), ('LLM', 'Master of Laws'), ('B.Arch', 'Bachelor of Architecture'), ('M.Arch', 'Master of Architecture'), ('B.Pharma', 'Bachelor of Pharmacy'), ('M.Pharma', 'Master of Pharmacy'), ('B.Sc Nursing', 'Bachelor of Science in Nursing'), ('M.Sc Nursing', 'Master of Science in Nursing'), ('BDS', 'Bachelor of Dental Surgery'), ('MDS', 'Master of Dental Surgery'), ('MBBS', 'Bachelor of Medicine and Bachelor of Surgery'), ('MD', 'Doctor of Medicine'), ('MS', 'Master of Surgery'), ('DM', 'Doctorate of Medicine'), ('M.Ch', 'Master of Chirurgiae'), ('Diploma', 'Diploma'), ('PG Diploma', 'Post Graduate Diploma'), ('Ph.D', 'Doctor of Philosophy'), ('M.Phil', 'Master of Philosophy'), ('LLB', 'Bachelor of Laws'), ('LLM', 'Master of Laws'), ('B.Arch', 'Bachelor of Architecture'), ('M.Arch', 'Master of Architecture'), ('B.Pharma', 'Bachelor of Pharmacy'), ('M.Pharma', 'Master of Pharmacy'), ('B.Sc Nursing', 'Bachelor of Science in Nursing'), ('M.Sc Nursing', 'Master of Science in Nursing'), ('BDS', 'Bachelor of Dental Surgery'), ('MDS', 'Master of Dental Surgery'), ('MBBS', 'Bachelor of Medicine and Bachelor of Surgery'), ('MD', 'Doctor of Medicine'), ('MS', 'Master of Surgery'), ('DM', 'Doctorate of Medicine'), ('M.Ch', 'Master of Chirurgiae'), ('Diploma', 'Diploma'), ('PG Diploma', 'Post Graduate Diploma'), ('Ph.D', 'Doctor of Philosophy'), ('M.Phil', 'Master of Philosophy'), ('LLB', 'Bachelor of Laws'), ('LLM', 'Master of Laws'), ('B.Arch', 'Bachelor of Architecture'), ('M.Arch', 'Master of Architecture'), ('B.Pharma', 'Bachelor of Pharmacy'), ('M.Pharma', 'Master of Pharmacy'), ('B.Sc Nursing', 'Bachelor of Science in Nursing'), ('M.Sc Nursing', 'Master of Science in Nursing'), ('BDS', 'Bachelor of Dental Surgery'), ('MDS', 'Master of Dental Surgery'), ('MBBS', 'Bachelor of Medicine and Bachelor of Surgery'), ('MD', 'Doctor of Medicine'), ('MS', 'Master of Surgery'), ('DM', 'Doctorate of Medicine'), ('M.Ch', 'Master of Chirurgiae'), ('Diploma', 'Diploma'), ('PG Diploma', 'Post Graduate Diploma'), ('Ph.D', 'Doctor of Philosophy')], max_length=20)),
                ('ID_number', models.CharField(max_length=20, unique=True)),
                ('previous_school', models.CharField(blank=True, max_length=150, null=True)),
                ('marks_percentage', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
