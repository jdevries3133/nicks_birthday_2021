from unittest import TestCase

from ..final_mode import FinalMode, shaify


def test_shaify():
    """
    I made these hashes with a common online tool, so I'm basically making
    sure that my way of doing things fits with the implementations of
    SHA256 that those common little tools use.
    """
    expect = [
        'd0e3df16a7ae644e021b8afe9e56bf1f6d78e4065d786c919a258a61e4b2bd84',
        'bb0347a468d97e98a9c00e37cebec1ab930f6f1221cae0f1fbb92b07e1900ba2',
        'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb',
        '489f719cadf919094ddb38e7654de153ac33c02febb5de91e5345cbe372cf4a0',
        '0422d42c689b7e8046dba2d7042e855f6d21e04464bab168fd263f5b10f893ed',
        'd7439c4d3981a069260a1b2989d90e549c4c8d7bc62c4f27bc51a7d7a73d90bf',
        'bb7208bc9b5d7c04f1236a82a0093a5e33f40423d5ba8d4266f7092c3ba43b62',
        '9f4024faec10ef6d29aa32d7935d94b1a816fd4fe0359fbf12d49d44b5ff33b8',
        'bcb9dae6ea88dbf28c262998e6661ec60f32a760faa5aef96745b39c38dbf235',
        '6fe8ecbc1deafa51c2ecf088cf364eba1ceba9032ffbe2621e771b90ea93153d',
        '6201111b83a0cb5b0922cb37cc442b9a40e24e3b1ce100a4bb204f4c63fd2ac0',
        '0ffb02665035bfe509b1d7c74f9abc481c2dbb4cb2db33b1116c22f2e686ef9f',
    ]
    result = shaify(
        'wishing you a happy birthday Nick! Love mom dad and Lola'
    )
    assert result == expect

class TestFinalMode(TestCase):

    maxDiff = None

    def setUp(self):
        self.fm = FinalMode()

    def test_puzzle_response(self):
        self.assertEqual(
            self.fm.puzzle_response('anything'),
            'If you need a hint, just say so!'
        )

    def test_check_answer(self):
        self.assertFalse(self.fm.check_answer('anything'))

    def test_check_hint(self):
        """
        This is shaified garbledness of the long HINT_MSG string you can
        see in the implementation.
        """
        hint = self.fm.hint()
        expect = (
            'fb1df1a24e3f6a12ee1fcb639a5c6d61d7919dc10ccb363b7ed75303b0391798\n'
            'd03502c43d74a30b936740a9517dc4ea2b2ad7168caa0a774cefe793ce0b33e7\n'
            'a83dd0ccbffe39d071cc317ddf6e97f5c6b1c87af91919271f9fa140b0508c6c\n'
            '49000c4444d51233fa10ad2015daccdef4ca48f3e5d1c99b98b295ea22071532\n'
            'bb0347a468d97e98a9c00e37cebec1ab930f6f1221cae0f1fbb92b07e1900ba2\n'
            'ba78973ddcf98d4e5369f5e722d681d94f5106895e5d6cf6fa3ca8240fabdc14\n'
            '14f22c3ccfb754c8a1e6fd94f9f6f36e0415243d0ea0d1aef49822e6ca325425\n'
            '10c22bcf4c768b515be4e94bcafc71bf3e8fb5f70b2584bcc8c7533217f2e7f9\n'
            'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb\n'
            '39c42dbad94bee80325b8eaa708521a788d5e5e29a5701f00529202db6c317f9\n'
            '1b001706a418bdfca35361355c643b7918572b8f9b7503f3043a6e23b45dce52\n'
            'cdb4ee2aea69cc6a83331bbe96dc2caa9a299d21329efb0336fc02a82e1839a8\n'
            '9f98b7c7f071714517d9a5e67c135b41fa3e91f20bac108158b33b073396f6e5\n'
            'e0e6c2af073e4c0724a6532cc20a30a2bc8f20d054dbc03457e2304f4381b249\n'
            '7b0363b65576ead3e362cc81287dad95d77146f76802ce0688e4e91adb7112eb\n'
            'cdb4ee2aea69cc6a83331bbe96dc2caa9a299d21329efb0336fc02a82e1839a8\n'
            '559aead08264d5795d3909718cdd05abd49572e84fe55590eef31a88a08fdffd\n'
            '38a81e87e79631e602bf5fbd307ce2fcd382b1670c585ea09032aac778a80531\n'
            '6ed0337140bd32b4adc5000f76333bd8ca6b2b2c9e0bc354335cf341456290e8\n'
            'fa51fd49abf67705d6a35d18218c115ff5633aec1f9ebfdc9d5d4956416f57f6\n'
            'e244f187f696561d5fd7e00f618e7ba641dc52e3c137380f6fa23a854b773aac\n'
            '10c22bcf4c768b515be4e94bcafc71bf3e8fb5f70b2584bcc8c7533217f2e7f9\n'
            'bb0347a468d97e98a9c00e37cebec1ab930f6f1221cae0f1fbb92b07e1900ba2\n'
            '663ea1bfffe5038f3f0cf667f14c4257eff52d77ce7f2a218f72e9286616ea39\n'
            'd05aa2a15fb3c40efeeb03bec445393f00074484cf01c8fb2da90ca6695a5531\n'
            'c0cafcf0e2d6a236aca78b03f4c33b25ca970788fd6adde4ccc7db6acecb3ee1\n'
            '8e7fc0236af43df9340685fc16f1efe36543cc1707051220a103ad99cf69a2df\n'
            'bb0347a468d97e98a9c00e37cebec1ab930f6f1221cae0f1fbb92b07e1900ba2\n'
            'cd1bb3012bcfaa0c50e954d03634f33c883c2478584e96f03d0d4b984bc6eadc\n'
            '749ab2c0d06c42ae3b841b79e79875f02b3a042e43c92378cd28bd444c04d284\n'
            '24065231df1b28929df88139f986d509bc2aed39f17c7566cea5d0f25e7f299f\n'
            'bb0347a468d97e98a9c00e37cebec1ab930f6f1221cae0f1fbb92b07e1900ba2\n'
            '15bd52797d7d181ee7f58e92b9a3b5be24a208f3a98918f9fe7591aff7b2781b\n'
            '663ea1bfffe5038f3f0cf667f14c4257eff52d77ce7f2a218f72e9286616ea39\n'
            'ac0b52a2ae6ef99999bc08fb31e19188bf0085a4614204068e677e140e1458be\n'
            'c6c1c9a9c8543f1e4cd980064cf1625eeb61a90703b2464fff039f21682508b3\n'
            'bb7208bc9b5d7c04f1236a82a0093a5e33f40423d5ba8d4266f7092c3ba43b62\n'
            'bdc7e96514483428984b8dc5197479b3cdc3e492a0264b5d6d0cc6987636dcb9\n'
            'd03502c43d74a30b936740a9517dc4ea2b2ad7168caa0a774cefe793ce0b33e7\n'
            'a83dd0ccbffe39d071cc317ddf6e97f5c6b1c87af91919271f9fa140b0508c6c\n'
            'ab6db599234d2636659cba1aa191bd014c3867d5cfade98ff694785c20c28fc6\n'
            '489f719cadf919094ddb38e7654de153ac33c02febb5de91e5345cbe372cf4a0\n'
            '663ea1bfffe5038f3f0cf667f14c4257eff52d77ce7f2a218f72e9286616ea39\n'
            '879915cfdc2cb4852ed05241911d8de5ca6e2cc4085746c14f13ad304157e264\n'
            'bb0347a468d97e98a9c00e37cebec1ab930f6f1221cae0f1fbb92b07e1900ba2\n'
            '8e7fc0236af43df9340685fc16f1efe36543cc1707051220a103ad99cf69a2df\n'
            'a83dd0ccbffe39d071cc317ddf6e97f5c6b1c87af91919271f9fa140b0508c6c\n'
            'ab6db599234d2636659cba1aa191bd014c3867d5cfade98ff694785c20c28fc6\n'
            'fcec91509759ad995c2cd14bcb26b2720993faf61c29d379b270d442d92290eb\n'
            '10c22bcf4c768b515be4e94bcafc71bf3e8fb5f70b2584bcc8c7533217f2e7f9\n'
            'bb0347a468d97e98a9c00e37cebec1ab930f6f1221cae0f1fbb92b07e1900ba2\n'
            'd03502c43d74a30b936740a9517dc4ea2b2ad7168caa0a774cefe793ce0b33e7\n'
            '038468518ad8122e13112743f890c7ba96ac5665b71de548eceb23e9ef237805\n'
            '48b676e2b107da679512b793d5fd4cc4329f0c7c17a97cf6e0e3d1005b600b03\n'
            'cdb4ee2aea69cc6a83331bbe96dc2caa9a299d21329efb0336fc02a82e1839a8\n'
            'a83dd0ccbffe39d071cc317ddf6e97f5c6b1c87af91919271f9fa140b0508c6c\n'
            '9cdc6c47aa193ae7fdab6c57a88f118e0adbe254c82095d39531f5e5c1314bdd\n'
            '8656aa55d393b032b7f05fd40daac127c4862315017072b231d726ccf0d686e6\n'
            '106a5842fc5fce6f663176285ed1516dbb1e3d15c05abab12fdca46d60b539b7\n'
            '663ea1bfffe5038f3f0cf667f14c4257eff52d77ce7f2a218f72e9286616ea39\n'
            '46599c5bb5c33101f80cea8438e2228085513dbbb19b2f5ce97bd68494d3344d\n'
            '97c10efe01d5c9c88704a12d361d8429b3a6aa2412290a0773109d5d2d603d5e\n'
            '663ea1bfffe5038f3f0cf667f14c4257eff52d77ce7f2a218f72e9286616ea39\n'
            'e6640de835ad09fb0a7367ee2e0ba99d0142c139db0272146e35538bd07479fc\n'
            'cdb4ee2aea69cc6a83331bbe96dc2caa9a299d21329efb0336fc02a82e1839a8\n'
            'fb1df1a24e3f6a12ee1fcb639a5c6d61d7919dc10ccb363b7ed75303b0391798\n'
            'd03502c43d74a30b936740a9517dc4ea2b2ad7168caa0a774cefe793ce0b33e7\n'
            '0695b563acde461fc2f8d9aebccf35c7596ac458b8d8e067c602fb7b4e5f1578\n'
            '8e7fc0236af43df9340685fc16f1efe36543cc1707051220a103ad99cf69a2df\n'
            '85574fa07dae32132675e21676042035c1b8a8384e11cd430269cff53f29add1\n'
            'fb46c79b7eb7af175f493755b491afa9b25574a9230b8822c629f224a2df4e58\n'
            'f9754b61f2b7ffbddab0f38f7bff938bcc981184d55d6dae507d245daa81437b\n'
            '14ebe56a5008e7c251101e9e1fdbe281ab0a82bd6fa00a5cef746b9ee0dd31d1\n'
            '1eb79602411ef02cf6fe117897015fff89f80face4eccd50425c45149b148408\n'
            '908aec4512d80ff4fefb1970899091e9de8e734b36b8fdb7678e77dc092f6959\n'
            'cdb4ee2aea69cc6a83331bbe96dc2caa9a299d21329efb0336fc02a82e1839a8\n'
            '1e3abf61a37e3cad36b11b459b1cc39e76feb6a0c369fe5270957468288dcc5c\n'
            'bb0347a468d97e98a9c00e37cebec1ab930f6f1221cae0f1fbb92b07e1900ba2\n'
            '9f584196e7fe6de85d3898bc0b11c78b1d0a1d49530ee5eaf7c26c3939cf043d\n'
            '3316348dbadfb7b11c7c2ea235949419e23f9fa898ad2c198f999617912a9925\n'
            '1eb79602411ef02cf6fe117897015fff89f80face4eccd50425c45149b148408\n'
            'd03502c43d74a30b936740a9517dc4ea2b2ad7168caa0a774cefe793ce0b33e7\n'
            '8e7fc0236af43df9340685fc16f1efe36543cc1707051220a103ad99cf69a2df\n'
            '70332d559269a27a08e8292a4582b0a39fc98bf0258f70d94e42a5adac26aebe\n'
            'bb0347a468d97e98a9c00e37cebec1ab930f6f1221cae0f1fbb92b07e1900ba2\n'
            '17b669561c95d3ac83bd5f4cbf7dea0041b3fe8b2302efaa4e7fc1582c591c4e\n'
            'b9776d7ddf459c9ad5b0e1d6ac61e27befb5e99fd62446677600d7cacef544d0\n'
            'b36fd74a8e0dc652645d44e57511b5b668158f7ac9aa7ae504885cf03eca4974\n'
            '6201111b83a0cb5b0922cb37cc442b9a40e24e3b1ce100a4bb204f4c63fd2ac0\n'
            'bcc649cfdb8cc557053da67df7e7fcb740dcf7f721cebe1f2082597ad0d5e7d8\n'
            'b9776d7ddf459c9ad5b0e1d6ac61e27befb5e99fd62446677600d7cacef544d0\n'
            'ab530a13e45914982b79f9b7e3fba994cfd1f3fb22f71cea1afbf02b460c6d1d\n'
            '75857a45899985be4c4d941e90b6b396d6c92a4c7437aaf0bf102089fe21379d\n'
            '8e7fc0236af43df9340685fc16f1efe36543cc1707051220a103ad99cf69a2df\n'
            'cf0622ef2a661cd2f11b0b644e40e4e00eb962918424a8c8ba53842fdf290235\n'
            '28391d3bc64ec15cbb090426b04aa6b7649c3cc85f11230bb0105e02d15e3624\n'
            '5eb2da9c26b65531549c8863fa023f9b48c1d3f0e17e01d7c4978876c724b21f\n'
            'cdb4ee2aea69cc6a83331bbe96dc2caa9a299d21329efb0336fc02a82e1839a8\n'
            'b708724a23bf11c2a5095adfe16cd12cda8c74437093bb2a33ea32850521f691\n'
            '8e7fc0236af43df9340685fc16f1efe36543cc1707051220a103ad99cf69a2df\n'
            '582967534d0f909d196b97f9e6921342777aea87b46fa52df165389db1fb8ccf\n'
            '1b001706a418bdfca35361355c643b7918572b8f9b7503f3043a6e23b45dce52\n'
            'd03502c43d74a30b936740a9517dc4ea2b2ad7168caa0a774cefe793ce0b33e7\n'
            'bb0347a468d97e98a9c00e37cebec1ab930f6f1221cae0f1fbb92b07e1900ba2\n'
            '193c45b5281908d2d9c814ba73be696dd3f252052c230f925d797f373f318d03\n'
            '749ab2c0d06c42ae3b841b79e79875f02b3a042e43c92378cd28bd444c04d284\n'
            'bb0347a468d97e98a9c00e37cebec1ab930f6f1221cae0f1fbb92b07e1900ba2\n'
            'be8dff00b0d468b29d804886729be5b430163ad625b1b621d943c2f80005281a\n'
            '663ea1bfffe5038f3f0cf667f14c4257eff52d77ce7f2a218f72e9286616ea39\n'
            '889393fb69a5b305188405f66dd58ca1fefad6cef46cfbf85236146e633f2a66\n'
            '762069bc07a6e1b5df123a5ae7bd91c10daa04694fbaa17fba0cd6a8dcce8f22\n'
            '8e7fc0236af43df9340685fc16f1efe36543cc1707051220a103ad99cf69a2df\n'
            '65f1688e72d6520249a107e8ff513715dfd232261f909b911d2b9dd27760093a\n'
            '82244417f956ac7c599f191593f7e441a4fafa20a4158fd52e154f1dc4c8ed92\n'
            'd80c9bf910f144738ef983724bc04bd6bd3f17c5c83ed57bedee1b1b9278e811\n'
            '8e7fc0236af43df9340685fc16f1efe36543cc1707051220a103ad99cf69a2df\n'
            'b9776d7ddf459c9ad5b0e1d6ac61e27befb5e99fd62446677600d7cacef544d0\n'
            '9d74932bdb6f21dc7ab21d6fc5260f474e0d538571fba7a82b74ffe47e6f9a10\n'
            '7afbb3347fb7252e533d58d99d72d9106fc6fdb3f30df23fa70b764c15ac42c5\n'
            'bb0347a468d97e98a9c00e37cebec1ab930f6f1221cae0f1fbb92b07e1900ba2\n'
            '3c482346f375027677fa8a0d6830a32714d4f13f9e94c2d9e215e0ac205ad4e5\n'
            '15eaa75240aed625be3e142205df3adbbb7051802b32f450e40276be8582b6d8\n'
            '1eb79602411ef02cf6fe117897015fff89f80face4eccd50425c45149b148408\n'
            '5ef5ef0364b6939c4ca61f34b393f7b368d1be8619647aaf83d5b395919ab629\n'
            '03494afd4248c42f5fa1237bf2eeebe751ab8d9c977d55405fcb17469dbd91f8\n'
            'bb7208bc9b5d7c04f1236a82a0093a5e33f40423d5ba8d4266f7092c3ba43b62\n'
            'c79cae2b47a69aa9b46e6def26e99a2780bda0ecfc1d9436563de3a7e7df9fe4\n'
            'acba25512100f80b56fc3ccd14c65be55d94800cda77585c5f41a887e398f9be\n'
            '4d040d3f6466018c568aadf69a666d4257e5bb350a8e06f7198aedb6b12386fe\n'
            '08951f270e19431ddc9bef08b442d526bb93b168823dbb5bbfdf97094315f611\n'
            'ab530a13e45914982b79f9b7e3fba994cfd1f3fb22f71cea1afbf02b460c6d1d\n'
            '9c6725dc269a48ce4b5bc78b580ccab2efbe6f3ccae64b1d44839f0cebd92fbe\n'
            'b3abe5d8c69b38733ad57ea75e83bcae42bbbbac75e3a5445862ed2f8a2cd677\n'
            'd03502c43d74a30b936740a9517dc4ea2b2ad7168caa0a774cefe793ce0b33e7\n'
            '21af6f1260f927f5b9b3ff5ca4a5d19493a1a47a5977240d8dca31bc47a63527\n'
            'd1905cf90af29a5ac3f99e105830eecc5b3b415b24e2d166a7ce4cf72b2f32e6\n'
            '8e7fc0236af43df9340685fc16f1efe36543cc1707051220a103ad99cf69a2df\n'
            '51e8ea280b44e16934d4d611901f3d3afc41789840acdff81942c2f65009cd52\n'
            'd0013c2e0a387e4c6e6962c5f4b0c9481d60fbb9eb425ae5cda2f8ceb2c0064f\n'
            '0bf474896363505e5ea5e5d6ace8ebfb13a760a409b1fb467d428fc716f9f284\n'
            '6201111b83a0cb5b0922cb37cc442b9a40e24e3b1ce100a4bb204f4c63fd2ac0\n'
            'a3b142af6e97cfc3bb23e409ab83467af7d16ded7dc0632be6a6a9023e49ce8b\n'
            '2ad8a7049d7c5511ac254f5f51fe70a046ebd884729056f0fe57f5160d467153\n'
            'f4bf9f7fcbedaba0392f108c59d8f4a38b3838efb64877380171b54475c2ade8\n'
            'b9776d7ddf459c9ad5b0e1d6ac61e27befb5e99fd62446677600d7cacef544d0\n'
            '7299453b621d99c8276fe0e83fa140072a0ab85e1a2be10331ff8f668db65b0c\n'
            '2c70e12b7a0646f92279f427c7b38e7334d8e5389cff167a1dc30e73f826b683\n'
            '663ea1bfffe5038f3f0cf667f14c4257eff52d77ce7f2a218f72e9286616ea39\n'
            'cdfbc38622aa09e0e72cb555d34693f2481200a5ed9802dc5ae7006a42956293\n'
            'b9776d7ddf459c9ad5b0e1d6ac61e27befb5e99fd62446677600d7cacef544d0\n'
            '0682c5f2076f099c34cfdd15a9e063849ed437a49677e6fcc5b4198c76575be5\n'
            'ab530a13e45914982b79f9b7e3fba994cfd1f3fb22f71cea1afbf02b460c6d1d\n'
            'cdb4ee2aea69cc6a83331bbe96dc2caa9a299d21329efb0336fc02a82e1839a8\n'
            'b6dd0a34d444d9a74a6e987d9686841c5abdc7b0e5c1c88505b9064217f39dd6\n'
            'bb7208bc9b5d7c04f1236a82a0093a5e33f40423d5ba8d4266f7092c3ba43b62'
        )
        self.assertEqual(hint, expect)
