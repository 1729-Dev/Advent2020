import factory
import uuid

from models.sampe import Sample

class SampleFactory(factory.Factory):
    class Meta:
        model = Sample

    failure_types = (
        'BUSY',
        'CANCELED',
        'OTHER',
        'UNKNOWN'
    )

    callId = factory.Faker('uuid4')
    callSid = factory.Faker('lexify', text='CA????????????????????????????????', letters='0123456789abcdefghijklmnopqrstuvwxyz')
    failureReason = factory.Faker('random_element', elements=failure_types)
    millisecondsFromEpoch = factory.Faker('pyint', min_value=int(time.time()), max_value=int(time.time())+500000)
    zip = factory.Faker("postcode_in_state", state_abbr="MN")
    city = factory.Faker("city")
    firstName = factory.Faker('first_name')
    lastName = factory.Faker('last_name')
    dateOfBirth = factory.Faker('date', pattern="%Y-%m-%d")


