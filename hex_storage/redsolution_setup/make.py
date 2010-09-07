from redsolutioncms.make import BaseMake
from redsolutioncms.models import CMSSettings

class Make(BaseMake):
    def make(self):
        super(Make, self).make()
        cms_settings = CMSSettings.objects.get_settings()
        cms_settings.render_to('settings.py', 'hex_storage/redsolutioncms/settings.pyt')

make = Make()

