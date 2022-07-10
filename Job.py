class Job(object):
    title = ""
    location = ""
    salary = 0
    experience = 0
    qualifications = []
    responsibilities = []

    def __init__(self, title, location, salary, experience, qualifications, responsibilities):
        self.title = title
        self.location = location
        self.salary = salary
        self.experience = experience
        self.qualifications = qualifications
        self.responsibilities = responsibilities

class LiteJob(object):
    title = ""
    location = ""
    posting_link = ""

    def __init__(self, title, location, posting_link):
        self.title = title
        self.location = location
        self.posting_link = posting_link

def make_job(title, location, salary, experience, qualifications, responsibilities):
    job = Job(title, location, salary, experience, qualifications, responsibilities)
    return job

def make_job_lite(title, location, posting_link):
    job = LiteJob(title, location, posting_link)
    return job


def print_job(self):
    print("Title: ", self.title)
    print("Location: ", self.location)
    print("Salary ", self.salary)
    print("Experience: ", self.experience)

    print("Qualifications: ")
    for x in self.qualifications:
        print(x)

    print("Responsibilities: ")
    for x in self.responsibilities:
        print(x)

def print_job_lite(self):
    print("Title: ", self.title)
    print("Location: ", self.location)
    print("Link ", self.posting_link)