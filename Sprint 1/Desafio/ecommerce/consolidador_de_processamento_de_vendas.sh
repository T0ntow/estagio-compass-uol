#!/bin/bash

# Caminho para os relatórios
caminho_relatorios="vendas/backup"

# Nome do arquivo final
relatorio_final="relatorio_final.txt"

# Remover relatório final anterior, se existir
rm -f "$relatorio_final"

# Loop pelos relatórios e concatenar ao relatório final
for relatorio in "$caminho_relatorios"/*.txt; do
    cat "$relatorio" >> "$relatorio_final"
done

echo "Relatório final consolidado gerado com sucesso em $relatorio_final"

