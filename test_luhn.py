import unittest
from luhn import Luhn

class TestLuhn(unittest.TestCase):
    def test_luhn_bad(self):
        invalids = ["883623", "11952012959", "28614472", "00562706", "129257468", "Hello", "This is Sparta!"]
        for invalid in invalids:
            luhn = Luhn()
            self.assertEquals(False, luhn.pass_luhn(invalid), "pass_luhn('" + invalid + "') failed")

    def test_luhn_good(self):
        numbers = ["33670704", "09174823721398", "1115490870", "99683526", "32999864"]
        for number in numbers:
            luhn = Luhn()
            self.assertEquals(True, luhn.pass_luhn(number), "pass_luhn('" + number + "') failed")

    def test_amex_good(self):
        numbers = ["375230543803415",
            "372855398479987",
            "348990244092295",
            "341503295748603",
            "379355667417001",
            "379426297832594",
            "371492942146432",
            "371700233046503",
            "378330498600605",
            "344543664068941"]
        for number in numbers:
            luhn = Luhn()
            self.assertEquals(True, luhn.is_amex(number), "is_amex('" + number + "') failed")

    def test_amex_bad(self):
        numbers = ["345098146192080",
            "347278442039013",
            "373965875681313",
            "379217156053966",
            "373684019678540",
            # close, but not quite - right start, pass Luhn, wrong length
            "341182728053",
            "340643093586",
            "341555338373",
            "37666663508385",
            "37675525006744",
            # Really wrong
            "howdy",
            "01234567890123456",
            "41231231231231231"]
        for number in numbers:
            luhn = Luhn()
            self.assertEquals(False, luhn.is_amex(number), "is_amex('" + number + "') failed")

    def test_discover_good(self):
        numbers =["6011235073010742",
            "6011524788676834",
            "6011158161407028",
            "6011766523035236",
            "6011150742532655",
            "6011166448556608",
            "6011324977616679",
            "6011839834433893",
            "6011552062373208",
            "6011444762962912"]
        for number in numbers:
            luhn = Luhn()
            self.assertEquals(True, luhn.is_discover(number), "is_discover('" + number + "') failed")

    def test_discover_bad(self):
        numbers =["6011487687621128",
            "6011778175463364",
            "6011131244530391",
            "6011514734292978",
            "6011542313142433",
            # close, but not quite - right start, pass Luhn, wrong length
            "60111092169087",
            "601134230558371",
            "60112632457580834",
            "601149551963210512",
            "6011531011661742466",
            # Really wrong
            "howdy",
            "01234567890123456",
            "41231231231231231"]
        for number in numbers:
            luhn = Luhn()
            self.assertEquals(False, luhn.is_discover(number), "is_discover('" + number + "') failed")

    def test_mastercard_bad(self):
        numbers = ["5143077456121267",
            "5113364355637234",
            "5197742932178218",
            "5401056202317764",
            "5314111834553318",
            # close, but not quite - right start, pass Luhn, wrong length
            "484847883876764",
            "434825549566376",
            "445534996525813",
            "438458030087292",
            "417550999305841",
            # Really wrong
            "howdy",
            "01234567890123456",
            "41231231231231231"]
        for number in numbers:
            luhn = Luhn()
            self.assertEquals(False, luhn.is_mastercard(number), "is_mastercard('" + number + "') failed")
    def test_mastercard_good(self):
        numbers = ["5452167326303681",
            "5307004215394397",
            "5459797393883992",
            "5383700309332774",
            "5480794366064505",
            "5202972394155274",
            "5365137870870308",
            "5312420331161861",
            "5278013211338261",
            "5287235603112439"]
        for number in numbers:
            luhn = Luhn()
            self.assertEquals(True, luhn.is_mastercard(number), "is_mastercard('" + number + "') failed")

    def test_visa_good(self):
        numbers = ["4205659557517",
            "4677280213639",
            "4215481871731316",
            "4244794944082",
            "4667017527708",
            "4305778575538363",
            "4072524749384",
            "4184442696606718",
            "4702035268645859",
            "4924665617046"]
        for number in numbers:
            luhn = Luhn()
            self.assertEquals(True, luhn.is_visa(number), "is_visa('" + number + "') failed")

    def test_visa_bad(self):
        numbers = ["4526403054202116",
            "4155600236541931",
            "4418974072850",
            "4652088193375180",
            "4352006227973",
            "4682830853770047",
            "4095023616634",
            "4131631722344547",
            "4689682909955443",
            "4763062663674525",
            # close, but not quite - right start, pass Luhn, wrong length
            "484847883876764",
            "434825549566376",
            "445534996525813",
            "438458030087292",
            "417550999305841",
            # Really wrong
            "howdy",
            "01234567890123456",
            "41231231231231231"]
        for number in numbers:
            luhn = Luhn()
            self.assertEquals(False, luhn.is_visa(number), "is_visa('" + number + "') failed")