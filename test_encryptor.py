import encryptor
import pytest


@pytest.mark.parametrize(
    "password,hash_,expected",
    [
        ["password", "hash:salt:1", False],
        ["password", "67a1e09bb1f83f5007dc119c14d663aa:salt:0", True],
        [
            "password",
            "13601bda4ea78e55a07b98866d2be6be0744e3866f13c00c811cab608a28f322:salt:1",
            True,
        ],
        [
            "password",
            "c6aad9e058f6c4b06187c06d2b69bf506a786af030f81fb6d83778422a68205e:salt:1:2",
            True,
        ],
        [
            "password",
            "3b68ca4706cbae291455e4340478076c1e1618e742b6144cfcc3e50f648903e4:salt:0:1",
            True,
        ],
    ],
)
def test_verify(password, hash_, expected):
    assert (
        encryptor.verify(password, hash_, keys=["g9mY9KLrcuAVJfsmVUSRkKFLDdUPVkaZ"])
        == expected
    )
