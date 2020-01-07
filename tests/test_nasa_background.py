"""
Tests for update()
"""
from datetime import datetime

import pytest
from click.testing import CliRunner

import nasa_background
from tools.background import change_background
from tools.nasa_api import get_info


# Test update --auto
def test_update_auto(mocker, DATE_IMG):
    mock_meta_info = {'title': 'test_title', 'explanation': 'test_explanation'}

    mock_get_info = mocker.patch(
        'tools.nasa_api.get_info', return_value=mock_meta_info)
    mock_download_image = mocker.patch(
        'tools.nasa_api.download_image', return_value='test_path')
    mock_change_background = mocker.patch('tools.background.change_background')

    runner = CliRunner()
    result = runner.invoke(nasa_background.update, ["--auto", "--date", f"{DATE_IMG.strftime('%Y-%m-%d')}"])
    assert result.exit_code == 0

    mock_get_info.assert_called_with(DATE_IMG)
    mock_download_image.assert_called_with(DATE_IMG)
    mock_change_background.assert_called_with('test_path', True)
