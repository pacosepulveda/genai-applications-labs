import pytest

from src.visual_provider import (
    MockVisualProvider,
    build_visual_provider,
)


def test_mock_provider_reproducible():
    provider = MockVisualProvider()

    a = provider.generate("ignored", 42)
    b = provider.generate("ignored", 42)

    assert a.image.tobytes() == b.image.tobytes()
    assert a.provider == "mock"


def test_build_mock():
    provider = build_visual_provider(
        "mock",
        "us-west-2",
        "example-model",
    )

    assert provider.name == "mock"


def test_unknown_provider():
    with pytest.raises(ValueError):
        build_visual_provider(
            "unknown",
            "us-west-2",
            "example-model",
        )
