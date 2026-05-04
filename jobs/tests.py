from django.test import TestCase
from .models import Job

class JobTestCase(TestCase):
    def test_create_job(self):
        job = Job.objects.create(
            title="Test",
            description="Test Desc",
            company="TestCo",
            location="TestLoc"
        )
        self.assertEqual(job.title, "Test")
