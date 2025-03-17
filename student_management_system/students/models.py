from django.db import models

# Create your models here.
class Student(models.Model):
    GENDER_CHOICES=[
        ('M','Male'),
        ('F','Female'),
        ('O','Other'),
    ]
    PROGRAM_NAME=[
        ('B.Tech','Bachelor of Technology'),
        ('M.Tech','Master of Technology'),
        ('B.Sc','Bachelor of Science'),
        ('M.Sc','Master of Science'),
        ('B.Com','Bachelor of Commerce'),
        ('M.Com','Master of Commerce'),
        ('B.A','Bachelor of Arts'),
        ('M.A','Master of Arts'),
        ('B.B.A','Bachelor of Business Administration'),
        ('M.B.A','Master of Business Administration'),
        ('B.C.A','Bachelor of Computer Applications'),
        ('M.C.A','Master of Computer Applications'),
        ('B.Ed','Bachelor of Education'),
        ('M.Ed','Master of Education'),
        ('B.Arch','Bachelor of Architecture'),
        ('M.Arch','Master of Architecture'),
        ('B.Pharma','Bachelor of Pharmacy'),
        ('M.Pharma','Master of Pharmacy'),
        ('B.Sc Nursing','Bachelor of Science in Nursing'),
        ('M.Sc Nursing','Master of Science in Nursing'),
        ('BDS','Bachelor of Dental Surgery'),
        ('MDS','Master of Dental Surgery'),
        ('MBBS','Bachelor of Medicine and Bachelor of Surgery'),
        ('MD','Doctor of Medicine'),
        ('MS','Master of Surgery'),
        ('DM','Doctorate of Medicine'),
        ('M.Ch','Master of Chirurgiae'),
        ('Diploma','Diploma'),
        ('PG Diploma','Post Graduate Diploma'),
        ('Ph.D','Doctor of Philosophy'),
        ('M.Phil','Master of Philosophy'),
        ('LLB','Bachelor of Laws'),
        ('LLM','Master of Laws'),
        ('B.Arch','Bachelor of Architecture'),
        ('M.Arch','Master of Architecture'),
        ('B.Pharma','Bachelor of Pharmacy'),
        ('M.Pharma','Master of Pharmacy'),
        ('B.Sc Nursing','Bachelor of Science in Nursing'),
        ('M.Sc Nursing','Master of Science in Nursing'),
        ('BDS','Bachelor of Dental Surgery'),
        ('MDS','Master of Dental Surgery'),
        ('MBBS','Bachelor of Medicine and Bachelor of Surgery'),
        ('MD','Doctor of Medicine'),
        ('MS','Master of Surgery'),
        ('DM','Doctorate of Medicine'),
        ('M.Ch','Master of Chirurgiae'),
        ('Diploma','Diploma'),
        ('PG Diploma','Post Graduate Diploma'),
        ('Ph.D','Doctor of Philosophy'),
        ('M.Phil','Master of Philosophy'),
        ('LLB','Bachelor of Laws'),
        ('LLM','Master of Laws'),
        ('B.Arch','Bachelor of Architecture'),
        ('M.Arch','Master of Architecture'),
        ('B.Pharma','Bachelor of Pharmacy'),
        ('M.Pharma','Master of Pharmacy'),
        ('B.Sc Nursing','Bachelor of Science in Nursing'),
        ('M.Sc Nursing','Master of Science in Nursing'),
        ('BDS','Bachelor of Dental Surgery'),
        ('MDS','Master of Dental Surgery'),
        ('MBBS','Bachelor of Medicine and Bachelor of Surgery'),
        ('MD','Doctor of Medicine'),
        ('MS','Master of Surgery'),
        ('DM','Doctorate of Medicine'),
        ('M.Ch','Master of Chirurgiae'),
        ('Diploma','Diploma'),
        ('PG Diploma','Post Graduate Diploma'),
        ('Ph.D','Doctor of Philosophy'),
        ('M.Phil','Master of Philosophy'),
        ('LLB','Bachelor of Laws'),
        ('LLM','Master of Laws'),
        ('B.Arch','Bachelor of Architecture'),
        ('M.Arch','Master of Architecture'),
        ('B.Pharma','Bachelor of Pharmacy'),
        ('M.Pharma','Master of Pharmacy'),
        ('B.Sc Nursing','Bachelor of Science in Nursing'),
        ('M.Sc Nursing','Master of Science in Nursing'),
        ('BDS','Bachelor of Dental Surgery'),
        ('MDS','Master of Dental Surgery'),
        ('MBBS','Bachelor of Medicine and Bachelor of Surgery'),
        ('MD','Doctor of Medicine'),
        ('MS','Master of Surgery'),
        ('DM','Doctorate of Medicine'),
        ('M.Ch','Master of Chirurgiae'),
        ('Diploma','Diploma'),
        ('PG Diploma','Post Graduate Diploma'),
        ('Ph.D','Doctor of Philosophy'),
        ('M.Phil','Master of Philosophy'),
        ('LLB','Bachelor of Laws'),
        ('LLM','Master of Laws'),
        ('B.Arch','Bachelor of Architecture'),
        ('M.Arch','Master of Architecture'),
        ('B.Pharma','Bachelor of Pharmacy'),
        ('M.Pharma','Master of Pharmacy'),
        ('B.Sc Nursing','Bachelor of Science in Nursing'),
        ('M.Sc Nursing','Master of Science in Nursing'),
        ('BDS','Bachelor of Dental Surgery'),
        ('MDS','Master of Dental Surgery'),
        ('MBBS','Bachelor of Medicine and Bachelor of Surgery'),
        ('MD','Doctor of Medicine'),
        ('MS','Master of Surgery'),
        ('DM','Doctorate of Medicine'),
        ('M.Ch','Master of Chirurgiae'),
        ('Diploma','Diploma'),
        ('PG Diploma','Post Graduate Diploma'),
        ('Ph.D','Doctor of Philosophy'),
    ]

    #Personal Details-------------
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=15)
    date_of_birth=models.DateField()
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES)
    address=models.TextField()
    nationality=models.CharField(max_length=50)
    profile_pic=models.ImageField(upload_to='profile_pics/',null=True,blank=True)

    #Guardian Details-------------------
    guardian_name=models.CharField(max_length=100)
    guardian_phone=models.CharField(max_length=15)
    guardian_email=models.EmailField(null=True,blank=True)
    guardian_relation=models.CharField(max_length=50)

    #Academic Details-----------------------
    admission_date=models.DateField(auto_now_add=True)
    course=models.CharField(max_length=150)
    program_name=models.CharField(max_length=20,choices=PROGRAM_NAME)
    ID_number=models.CharField(max_length=20,unique=True)
    previous_school=models.CharField(max_length=150,null=True,blank=True)
    marks_percentage=models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)

    #extra-details----------------------
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} ({self.ID_number})"

