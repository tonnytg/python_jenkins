import os
import jenkins

# Get environment variables
jenkins_url = os.getenv('JENKINS_URL')
jenkins_user = os.getenv('JENKINS_USER')
jenkins_password = os.getenv('JENKINS_PASSWORD')

# Create a connection instance to Jenkins
server = jenkins.Jenkins(jenkins_url, username=jenkins_user, password=jenkins_password)

# Job name
job_name = 'PrintMessage'

# Job parameters
parameters = {
    'Name': 'Antonio',
    'Message': 'Hello world'
}

# Execute the job with the parameters
server.build_job(job_name, parameters)

print(f'Job {job_name} has been started with parameters {parameters}')

