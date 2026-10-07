import pytest

from src.visual_provider import MockVisualProvider, build_visual_provider


def test_mock_provider_is_reproducible_with_same_seed():
    provider = MockVisualProvider()

    a = provider.generate("ignored by mock", 42)
    b = provider.generate("ignored by mock", 42)

    assert a.image.tobytes() == b.image.tobytes()
    assert a.provider == "mock"


def test_build_mock_provider():
    provider = build_visual_provider(
        "mock",
        "us-west-2",
        "example-model",
    )
    assert provider.name == "mock"


def test_unknown_provider_raises():
    with pytest.raises(ValueError):
        build_visual_provider(
            "unknown",
            "us-west-2",
            "example-model",
        )
