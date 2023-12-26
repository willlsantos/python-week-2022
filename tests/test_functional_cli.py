# imita um usuário usando o programa
from typer.testing import CliRunner

from beerlog.cli import main

runner = CliRunner()

def test_add_beer():
    result = runner.invoke(
        main, ["add", "Colorado", "IPA", "--flavor=7", "--image=8", "--cost=6"]
    )
    assert result.exit_code == 0
    assert "🍻 Cerveja adicionada com sucesso!\n" in result.stdout