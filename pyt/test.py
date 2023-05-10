import socketio
from threading import Timer
# standard Python
sio = socketio.Client()
sio.connect('http://localhost:3100')
# sio.emit('identity', {'foo': 'bar'})

data = [
    {
        "aboutcompany": "Securin is obsessed with helping leaders continuously improve their security posture. We partner with our customers using our tech-enabled services including Attack Surface Management, Vulnerability Management, Pentesting and Vulnerability Intelligence. As a US Department of Homeland Security sponsored CVE number authority, we have deep expertise in offensive pentesting and unique insights into the latest threats. Our capabilities allow us to continuously reduce your attack surface and provide predictive intelligence, so you can stay ahead of the bad actors. At Securin, we work as an extension of your team, providing the glue to create a security fabric that protects your organization.",
        "aboutjob": "\nJob Title: Security Operations Center Analyst \nConsider joining a leading provider of Tech-enabled cybersecurity solutions in Albuquerque, NM!\nSecurin has been a leader in the cybersecurity industry. We have continuously improved the security posture of our customers against evolving and emerging cyber threats through our services in Vulnerability Management, Penetration Testing, Cloud security and a wide range of cybersecurity products. We are a Common Vulnerabilities and Exposures (CVE) Numbering Authority which is a US Department of Homeland Security-sponsored program that helps MITRE validate new vulnerabilities and expedite their entry into the National Vulnerability Database. CSW delivers its solutions effectively by combining human intelligence and automation while providing its customers with full coverage, extensive support, and guided remediation, helping them improve their security posture.\nAt Securin, we live by a people-first approach and we firmly believe that our employees should enjoy what they do. We provide a hybrid work environment with a competitive best in industry pay, providing an inclusive environment to learn, thrive, and grow. For the right candidate, this will feel like your second home!\nPlease note that we are prioritizing candidates who are interested and able to relocate to Albuquerque. A relocation package will be available to successful hires.\nTo learn more about us, please visit our website: https://www.securin.io \nJob Description:\nWe are seeking a highly motivated and experienced individual to join our team as a Security Operations Center (SOC) Analyst. As a SOC Analyst, you will be responsible for monitoring and analyzing security events and alerts generated by our security systems to identify potential threats and risks to our organization. You will be working in a fast-paced environment, collaborating with cross-functional teams to ensure the security and protection of our systems, data, and assets. Key Responsibilities:\nMonitor and analyze security events and alerts from various security systems, including intrusion detection and prevention systems, firewalls, and SIEM platforms.Conduct investigation and analysis of security incidents, including triage, identification, containment, eradication, and recovery activities.Develop and maintain incident response playbooks and procedures.Collaborate with cross-functional teams, including IT, engineering, and compliance, to ensure security incidents are appropriately managed and resolved.Participate in vulnerability management and threat intelligence activities.Provide regular reporting on security incidents, trends, and risks to management and stakeholders.Continuously monitor and assess the effectiveness of security controls and processes.\nRequirements:\nBachelor's degree in computer science, information security, or related field.At least 2-3 years of experience in a SOC analyst role or similar position.Solid understanding of information security principles and practices, including threat and vulnerability management, incident response, and security operations.Experience with security tools such as SIEM platforms, IDS/IPS, firewalls, and antivirus software.Knowledge of network protocols and operating systems, including Windows, Linux, and macOS.Strong analytical and problem-solving skills, with the ability to work well under pressure and manage multiple priorities.Excellent communication and collaboration skills, with the ability to work effectively in a team environment.Industry certifications such as CompTIA Security+, CEH, GIAC, or CISSP are preferred.Proficient in Python\nWork Conditions:\nRelocation to Albuquerque, NM is highly desirable2nd Shift (3pm - 12am) Monday thru Friday\nPowered by JazzHR\nVkpGtl7JhF\n ",
        "cinfo": [],
        "clogo": "https://media.licdn.com/dms/image/C560BAQEtUgtzA62YuQ/company-logo_100_100/0/1678117154024?e=2147483647&v=beta&t=eOEY6SrtW0vfcNoBip1CTpz3bQ8ERV_oVNVVtDAkI4c",
        "cname": "Securin Inc.",
        "companyabout": "https://www.linkedin.com/company/securin-inc/about",
        "companyattr": {
            "Attribute": [
                "https://securin.io",
                "505-302-1113\n            \n\n              Phone number is 505-302-1113",
                "IT Services and IT Consulting",
                "201-500 employees",
                "203 on LinkedIn\n            \n \n\n\n\n    Includes members with current employer listed as Securin Inc., including part-time roles.",
                "Albuquerque, New Mexico",
                "2020",
                "Penetration Testing, Attack Surface Management, Vulnerability Management as a Service, Threat Hunting, Vulnerability Research, Dark web mining, Penetration testing as a service, Red Teaming, Compliance Services, Predictive Early warning, and Vulnerability Intelligence"
            ],
            "Id": [
                "Website",
                "Phone",
                "Industry",
                "Company size",
                "Headquarters",
                "Founded",
                "Specialties"
            ]
        },
        "companyceo": "https://www.linkedin.com/company/securin-inc/people/?keywords=ceo",
        "companylink": "https://www.linkedin.com/company/securin-inc/",
        "jobtitle": "SOC Analyst",
        "link": "https://www.linkedin.com/jobs/view/soc-analyst-at-securin-inc-3602818870",
        "location": "Albuquerque, NM",
        "peoples": [
            {
                "email": "XXXXXXXXXXXXX",
                "link": "https://www.linkedin.com/in/guillermowhernandez?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAACUH7U0Bzl0mUZWHxe-0k-I6M_EaMxvGJ3U",
                "name": "Guillermo Hernandez",
                "phone": "XXXXXXXXXXXXX",
                "subtitle": "AI Solutions Architect at CYR3CON"
            }
        ],
        "time": "12 hours ago"
    },
    {
        "aboutcompany": "A team of eminent, distinguished and veteran professionals in the field of Talent Acquisition and Recruitment Consulting; scrutinize into every minor detail of the client’s requirement, while providing best solutions in strategic market networking, client acquisition and client servicing.  iStellarPro's  expertise includes GSA schedules,applications, and modifications; SBA program participation and compliance; proposal development (all proposal types); proposal writing/management\n\nAfter 15 years in the Talent Acquisition and Staffing industry, we decided to alter direction. Now, we share our passion by assisting your business. Our ramp up process is designed to empower your team. Stellar Professionals (iStellarPro) works on Lean Six Sigma based quality processes amalgamated with PRINCE2 project methodology to assist your business to kick-start growth in portfolio and revenue. The Company has direct and recent experience and contract wins in nearly every agency of the Federal Government including the Department of Homeland Security, Department of Defense, Department of State, Department of Energy, Department of Transportation, Department of Veterans Affairs, Department of Health and Human Services, and the intelligence community. \n\nBusiness mentors are key—  Stellar Professionals (iStellarPro)  continues to be relied upon by its customers as a trusted partner in their success. We have achieved this through the combination of best-in-class technology consultants and the smart use of standards in practices, procedures and methods. iStellarPro has developed practical methods and practices for effective technology delivery that has served our projects well in the form of predictable and consistent delivery. Our seasoned consultants pride themselves on having a blend of strong technology skills and a thorough understanding of business processes. This combination allows iStellarPro personnel to craft the most appropriate solution for the situations we’re confronted with. ",
        "aboutjob": "\nMode of interview: Web Cam Interview Only\n\nWork arrangement: Remote\n\nELECT - IT Security Analyst 4 - REMOTE\n\nApplicant must have 8 years of relevant experience with the following: \nExcellent drafting, writing, and analysis skillsOutstanding Problem Solving SkillsExperience drafting technical and administrative documentationDeveloping, creating, managing and maintaining security awareness programsEstablish and document Security ControlsDrafting Advanced Secuirty GovernanceExperience implementing advanced security governance and NIST 800-53CISSP\n ",
        "cinfo": [],
        "clogo": "https://media.licdn.com/dms/image/C4E0BAQGveZ81BUBqcg/company-logo_100_100/0/1607348675025?e=2147483647&v=beta&t=gUe03J4QJPPGcwV-QRWeKfYaYNrTikSm0kpZEjK7nEk",
        "cname": "Stellar Professionals",
        "companyabout": "https://www.linkedin.com/company/stellar-professionals/about",
        "companyattr": {
            "Attribute": [
                "https://iStellarPro.com",
                "3025004567\n            \n\n              Phone number is 3025004567",
                "Staffing and Recruiting",
                "11-50 employees",
                "24 on LinkedIn\n            \n \n\n\n\n    Includes members with current employer listed as Stellar Professionals, including part-time roles.",
                "Lewes, DE",
                "2019",
                "Bid Search, Capture Management, Proposal Writing, Proposal Management, Client Acquisition, Business Development, Pre-Sales, Staffing & Recruiting, Consulting, Account Management, Client Services, Service Management, IT Staffing, Non-IT Staffing, Public Sector Client Capture, Private Sector Client Capture, and Direct Clients"
            ],
            "Id": [
                "Website",
                "Phone",
                "Industry",
                "Company size",
                "Headquarters",
                "Founded",
                "Specialties"
            ]
        },
        "companyceo": "https://www.linkedin.com/company/stellar-professionals/people/?keywords=ceo",
        "companylink": "https://www.linkedin.com/company/stellar-professionals/",
        "jobtitle": "Remote: IT Security Analyst",
        "link": "https://www.linkedin.com/jobs/view/remote-it-security-analyst-at-stellar-professionals-3479432381",
        "location": "United States",
        "peoples": [
            {
                "email": "XXXXXXXXXXXXX",
                "link": "https://www.linkedin.com/in/sumitgagneja?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAABdGMmABhPi86tvGSrwZHtbGU5Nk9nrxrTA",
                "name": "Sumit Gagneja",
                "phone": "XXXXXXXXXXXXX",
                "subtitle": "Founder - Stellar Professionals | Facilitating and Nurturing U.S. Staffing startups and businesses to grow and sustain."
            }
        ],
        "time": "2 months ago"
    }
]
import random
def hello():
  
     sio.emit('identity', random.choice(data))
     Timer(2.0, hello).start()

Timer(2.0, hello).start() # after 30 seconds, "hello, world" will be printed

