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
