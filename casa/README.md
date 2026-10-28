# casa/ — cópia com hash do casa-poker (M5)

Cópia fixa do dado e do lint da casa, para o CI rodar num clone isolado (sem `../casa-poker` nem `../lastro`).

- `casa_lint.py` e `dados/banned_terms.json` vêm do casa-poker; `casa.lock.json` guarda os sha256 conferidos contra `_ops/validacao/casa.lock` da HUB.
- Conferir: `python casa/casa_lint.py hash --lock casa/casa.lock.json casa/dados/banned_terms.json` (o `casa_lint.py` é conferido por `scripts/casa-lint-ci.py --so-hash`).
- **Não edite à mão.** Para atualizar, a HUB muda o lock por `/mudar-contrato` e a cópia é refeita do casa-poker.
- CI: `.github/workflows/casa-lint.yml` → `scripts/casa-lint-ci.py`. Só erro em linha adicionada ou alterada pelo PR bloqueia; o resto é aviso e item de limpeza.
