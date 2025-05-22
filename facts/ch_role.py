'''Get the role from a managed preferences domain '''
from CoreFoundation import CFPreferencesCopyAppValue

def fact():
    role = CFPreferencesCopyAppValue('Role', 'uk.gov.companieshouse.role')
    if role is not None:
        return {'ch_role': role}
    return {'ch_role': 'Unknown'}

if __name__ == '__main__':
    print(fact())

