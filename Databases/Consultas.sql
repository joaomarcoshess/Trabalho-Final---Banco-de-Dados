# Consulta a
SELECT d.id AS "id da doença", d.nome AS Nome, d.cid AS CID, t.tipo AS "Tipo do patôgeno"
FROM doenca AS d
JOIN patogeno AS p
ON d.patogeno_id = p.id
JOIN TipoDePatogeno AS t
ON t.id = p.tipopatogeno_id
ORDER BY d.nome ASC;

# Consulta b
SELECT s.nome AS "nome do sintoma", t.nivel_ocorrencia AS "taxa de ocorrencia"
FROM Sintoma AS s
JOIN TaxaDeOcorrencia AS t
ON s.id = t.sintoma_id
WHERE t.doenca_id = 35
ORDER BY 
	CASE 
		WHEN t.nivel_ocorrencia = 'muito comum' THEN 1
		WHEN t.nivel_ocorrencia = 'comum' THEN 2
		WHEN t.nivel_ocorrencia = 'pouco comum' THEN 3
		WHEN t.nivel_ocorrencia = 'raro' THEN 4
		ELSE 5
	END,
	s.nome;
	
# Consulta c
SELECT d.id AS "id da doenca", d.nome AS "nome da doenca", 
	GROUP_CONCAT(CONCAT(s.nome, ' (', t.nivel_ocorrencia, ')') ORDER BY 
		CASE 
			WHEN t.nivel_ocorrencia = 'muito comum' THEN 1
			WHEN t.nivel_ocorrencia = 'comum' THEN 2
			WHEN t.nivel_ocorrencia = 'pouco comum' THEN 3
			WHEN t.nivel_ocorrencia = 'raro' THEN 4
			ELSE 5
		END
		SEPARATOR ', ') AS sintomas
FROM Doenca AS d
JOIN TaxaDeOcorrencia AS t
ON d.id = t.doenca_id
JOIN Sintoma AS s
ON t.sintoma_id = s.id
GROUP BY d.id
ORDER BY d.nome;

# Consulta d
SELECT t.tipo, COUNT(*) AS total
FROM doenca AS d
JOIN patogeno AS p
ON d.patogeno_id = p.id
JOIN TipoDePatogeno AS t
ON t.id = p.tipopatogeno_id
GROUP BY t.tipo
ORDER BY total DESC, t.tipo asc;

# Consulta e
SELECT
    (SELECT COUNT(*) FROM Doenca) AS numero_de_doencas,
    (SELECT COUNT(*) FROM Sintoma) AS numero_de_sintomas,
    AVG(num_sintomas) AS numero_medio_de_sintomas_por_doenca,
    MIN(num_sintomas) AS menor_numero_de_sintomas_de_uma_doenca,
    MAX(num_sintomas) AS maior_numero_de_sintomas_de_uma_doenca
FROM (
    SELECT COUNT(t.sintoma_id) AS num_sintomas
    FROM TaxaDeOcorrencia AS t
    JOIN Doenca AS d
	 ON d.id = t.doenca_id
    GROUP BY d.id
) AS subquery;

# Consulta f
SELECT s.nome AS nome_sintoma,
	COUNT(DISTINCT t.doenca_id) AS total_doencas,
   SUM(CASE WHEN t.nivel_ocorrencia = 'muito comum' THEN 1 ELSE 0 END) AS muito_comum,
	SUM(CASE WHEN t.nivel_ocorrencia = 'comum' THEN 1 ELSE 0 END) AS comum,
	SUM(CASE WHEN t.nivel_ocorrencia = 'pouco comum' THEN 1 ELSE 0 END) AS pouco_comum,
	SUM(CASE WHEN t.nivel_ocorrencia = 'raro' THEN 1 ELSE 0 END) AS raro,
	SUM(CASE WHEN t.nivel_ocorrencia = 'muito raro' THEN 1 ELSE 0 END) AS muito_raro
FROM Sintoma s
LEFT JOIN TaxaDeOcorrencia t ON s.id = t.sintoma_id
GROUP BY s.nome
ORDER BY total_doencas DESC, 
	CASE 
		WHEN MAX(CASE WHEN t.nivel_ocorrencia = 'muito comum' THEN 1 ELSE 0 END) = 1 THEN 1
		WHEN MAX(CASE WHEN t.nivel_ocorrencia = 'comum' THEN 1 ELSE 0 END) = 1 THEN 2
		WHEN MAX(CASE WHEN t.nivel_ocorrencia = 'pouco comum' THEN 1 ELSE 0 END) = 1 THEN 3
		WHEN MAX(CASE WHEN t.nivel_ocorrencia = 'raro' THEN 1 ELSE 0 END) = 1 THEN 4
		WHEN MAX(CASE WHEN t.nivel_ocorrencia = 'muito raro' THEN 1 ELSE 0 END) = 1 THEN 5
	END,
   s.nome;
   
# Consulta g
SELECT D.id, D.nome
FROM Doenca D
JOIN TaxaDeOcorrencia T1 ON D.id = T1.doenca_id
JOIN Sintoma S1 ON T1.sintoma_id = S1.id
JOIN TaxaDeOcorrencia T2 ON D.id = T2.doenca_id
JOIN Sintoma S2 ON T2.sintoma_id = S2.id
WHERE S1.nome = 'Febre' AND S2.nome = 'Diarreia'
ORDER BY D.nome;

# Consulta h
SELECT d.id AS "Doenca id", d.nome AS "Doenca nome",
	SUM(
		CASE 
		   WHEN t.sintoma_id IN (1, 2, 3, 4) THEN #Lista de sintomas
				CASE nivel_ocorrencia
					WHEN 'muito comum' THEN 5
					WHEN 'comum' THEN 4
					WHEN 'pouco comum' THEN 3
					WHEN 'raro' THEN 2
					WHEN 'muito raro' THEN 1
					ELSE 0
				END
		   ELSE 0
		END
	) - 
	(SELECT COUNT(*)
		FROM Sintoma s
		LEFT JOIN TaxaDeOcorrencia t
		ON s.id = t.sintoma_id AND t.doenca_id = d.id
		WHERE s.id IN (1, 2, 3, 4) -- Lista de sintomas
			AND t.sintoma_id IS NULL
	) AS pontuacao
FROM Doenca AS d
LEFT JOIN taxadeocorrencia AS t ON d.id = t.doenca_id
LEFT JOIN Sintoma s ON t.sintoma_id = s.id
GROUP BY d.id
ORDER BY pontuacao DESC;