class Profile:

    ATTRS = ['first_name','last_name','occupation','public_identifier',
            'industry','location','entity_urn','company_name','company_id',
            'connection_requested']

    def __init__(self,first_name,last_name,occupation,public_identifier,
            industry=None,location=None,entity_urn=None,company_name=None,
            company_id=None,connection_requested=False):

        industry = industry or ''
        location = location or ''
        entity_urn = entity_urn or ''
        company_name = company_name or ''
        company_id = company_id or ''

        if connection_requested and connection_requested == 'False':
            connection_requested = False
        elif connection_requested == 'True':
            connection_requested = True

        self.first_name = first_name
        self.last_name = last_name
        self.occupation = occupation
        self.public_identifier = public_identifier
        self.pid = self.public_identifier
        self.industry = industry
        self.location = location
        self.entity_urn = entity_urn
        self.company_name = company_name
        self.company_id = company_id
        self.connection_requested = connection_requested

    def __repr__(self):

        return f'< Profile: first_name:"{self.first_name}" ' \
               f'last_name:"{self.last_name}" ' \
               f'occupation:"{self.occupation}" ' \
               f'company_name:"{self.company_name}" ' \
               f'company_id:"{self.company_id}" >'

    def __eq__(self,other):
        '''Compare the PID of two Profile objects to determine
        if they're the same profile.
        '''

        if other.__class__ != Profile: return False
        return self.pid == other.pid

    def to_row(self):
        '''Translate the `Profile` object to a `list` that can then
        be written to disk as a CSV row.
        '''

        return [self.__getattribute__(a) for a in Profile.ATTRS]

    @staticmethod
    def from_row(row,headers):
        '''Translate a CSV (array) row to a Profile object. The CSV row
        should have been extracted from an output file generated by
        Peasant. The headers value is also an array containing the
        header row from the CSV file, allowing for the logic to map the
        attributes back to CSV values based on offset.
        '''

        return Profile(**{column:row[headers.index(column)]
                for column in headers})
