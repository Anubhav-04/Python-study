def personalDetails():
    name = 'Anubhav Kumar'
    Age = 28
    sex = 'M'
    M_no = '6202416753'
    return f'''Personal Details
        Name - {name}
        Age - {Age}Yrs 
        Sex - {sex} 
        Mobile Number - {M_no}'''

def officialDetails():
    id = 'Assar00879'
    Domain = 'Software Engineer'
    skills = 'Fullstack Java Development'
    organization = 'Google Cloud'
    return f'''Official details --------
            Id - {id}
            Domain - {Domain}
            skills - {skills}
            Organization - {organization}
'''
if (__name__ == '__main__'):
    print("The program is directly running from the source file")