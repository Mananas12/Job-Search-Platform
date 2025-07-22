from abc import ABC, abstractmethod
from validators import StringValidator, ContactValidator
 
class Company:
    name = StringValidator()
    contact_info = ContactValidator()
 
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.jobs = []
 
    def add_job(self, job):
        self.jobs.append(job)
 
    def list_jobs(self):
        return [job.display() for job in self.jobs]
 
class JobPosting(ABC):
    title = StringValidator()
    description = StringValidator()
 
    def __init__(self, title, description, salary, company):
        self.title = title
        self.description = description
        self.salary = salary
        self.company = company
 
    @abstractmethod
    def display(self):
        pass
 
class FullTimeJob(JobPosting):
    def display(self):
        return f"Full-Time: {self.title}, Salary: {self.salary}, Company: {self.company.name}"
 
class PartTimeJob(JobPosting):
    def __init__(self, title, description, salary, company, hours):
        super().__init__(title, description, salary, company)
        self.hours = hours
 
    def display(self):
        return f"Part-Time: {self.title}, Salary: {self.salary}, Hours: {self.hours}, Company: {self.company.name}"
 
class JobSeeker:
    name = StringValidator()
    contact_info = ContactValidator()
 
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.applied = []
 
    def apply(self, job):
        self.applied.append(job)
        print(f"{self.name} applied for {job.title}")
 
    def search_jobs(self, job_list, title=None, salary=None):
        result = job_list
        if title:
            result = [j for j in result if title.lower() in j.title.lower()]
        if salary:
            result = [j for j in result if j.salary >= salary]
        return result
 
if name == "__main__":
    c = Company("ArmeniaTech", "+37477123456")
    j1 = FullTimeJob("Backend Developer", "Work with Python", 5000, c)
    j2 = PartTimeJob("Junior Developer", "Learn and assist", 2000, c, 20)
    c.add_job(j1)
    c.add_job(j2)
 
    seeker = JobSeeker("Mariam", "+37477987654")
    for job in seeker.search_jobs(c.jobs, title="Developer", salary=3000):
        print(job.display())
        seeker.apply(job)
