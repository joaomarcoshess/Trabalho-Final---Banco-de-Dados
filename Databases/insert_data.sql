INSERT INTO TipoDePatogeno (tipo) VALUES 
	('Bactéria'),
	('Vírus'),
	('Parasita'),
	('Fungo');

INSERT INTO Patogeno (nome_cientifico, tipopatogeno_id) VALUES 
	('Mycobacterium tuberculosis', 1), -- Bactéria
	('Influenza virus', 2),            -- Vírus
	('Plasmodium spp.', 3),            -- Parasita
	('Dengue virus', 2),               -- Vírus
	('Hepatitis B virus', 2),          -- Vírus
	('Treponema pallidum', 1),         -- Bactéria
	('Candida albicans', 4),           -- Fungo
	('Varicella-zoster virus', 2),     -- Vírus
	('Leptospira spp.', 1),            -- Bactéria
	('Toxoplasma gondii', 3),          -- Parasita
	('Neisseria meningitidis', 1),     -- Bactéria
	('Yellow fever virus', 2),         -- Vírus
	('Zika virus', 2),                 -- Vírus
	('Chikungunya virus', 2),          -- Vírus
	('Rubella virus', 2),              -- Vírus
	('Measles virus', 2),              -- Vírus
	('Clostridium tetani', 1),         -- Bactéria
	('Mycobacterium leprae', 1),       -- Bactéria
	('Vibrio cholerae', 1),            -- Bactéria
	('Salmonella typhi', 1),           -- Bactéria
	('Poliovirus', 2),                 -- Vírus
	('Rabies virus', 2),               -- Vírus
	('Schistosoma spp.', 3),           -- Parasita
	('Giardia lamblia', 3),            -- Parasita
	('Entamoeba histolytica', 3),      -- Parasita
	('Trichomonas vaginalis', 3),      -- Parasita
	('Trypanosoma cruzi', 3),          -- Parasita
	('Leishmania spp.', 3),            -- Parasita
	('Hepatitis A virus', 2),          -- Vírus
	('Hepatitis C virus', 2),          -- Vírus
	('Herpes simplex virus', 2),       -- Vírus
	('Variola virus', 2),              -- Vírus
	('Epstein-Barr virus', 2),         -- Vírus
	('Mumps virus', 2);                -- Vírus

INSERT INTO Doenca (nome, cid, patogeno_id) VALUES
	('Tuberculose', 'A15-A19', 1),
	('Gripe', 'J10-J11', 2),
	('Malária', 'B50-B54', 3),
	('Dengue', 'A90', 4),
	('Hepatite B', 'B16', 5),
	('Sífilis', 'A50-A53', 6),
	('Candidíase', 'B37', 7),
	('Varicela', 'B01', 8),
	('Leptospirose', 'A27', 9),
	('Toxoplasmose', 'B58', 10),
	('Meningite', 'G00-G03', 11),
	('Febre Amarela', 'A95', 12),
	('Zika', 'A92.5', 13),
	('Chikungunya', 'A92.0', 14),
	('Rubéola', 'B06', 15),
	('Sarampo', 'B05', 16),
	('Tétano', 'A33-A35', 17),
	('Hanseníase', 'A30', 18),
	('Cólera', 'A00', 19),
	('Tifoide', 'A01.0', 20),
	('Poliomielite', 'A80', 21),
	('Raiva', 'A82', 22),
	('Esquistossomose', 'B65', 23),
	('Giardíase', 'A07.1', 24),
	('Amebíase', 'A06', 25),
	('Tricomoníase', 'A59', 26),
	('Doença de Chagas', 'B57', 27),
	('Leishmaniose', 'B55', 28),
	('Tétano Neonatal', 'A33', 17),
	('Hepatite A', 'B15', 29),
	('Hepatite C', 'B17.1', 30),
	('Herpes Simples', 'B00', 31),
	('Varíola', 'B03', 32),
	('Mononucleose', 'B27', 33),
	('Caxumba', 'B26', 34);
	
INSERT INTO NomesPopulares (nomes_populares, doenca_id) VALUES
	('Sapinho', 7),
	('Catapora', 8),
	('Lepra', 18),
	('Barriga d’água', 23),
	('Doença do Beijo', 34),
	('Papeira', 35);

INSERT INTO Sintoma (nome) VALUES 
	('Tosse'),
	('Febre'),
	('Perda de peso'),
	('Dor de cabeça'),
	('Fadiga'),
	('Calafrios'),
	('Dor muscular'),
	('Erupção cutânea'),
	('Icterícia'),
	('Dor abdominal'),
	('Úlceras'),
	('Coceira'),
	('Corrimento'),
	('Dor ao urinar'),
	('Rigidez de nuca'),
	('Dor articular'),
	('Espasmos musculares'),
	('Manchas na pele'),
	('Perda de sensibilidade'),
	('Fraqueza muscular'),
	('Diarreia'),
	('Vômito'),
	('Desidratação'),
	('Paralisia'),
	('Inchaço no local da picada'),
	('Feridas na pele'),
	('Inchaço das glândulas'),
	('Dor de garganta'),
	('Náusea'),
	('Ínguas'),
	('Rigidez'),
	('Feridas');

INSERT INTO TaxaDeOcorrencia (doenca_id, sintoma_id, nivel_ocorrencia) VALUES
	(1, 1, 'muito comum'), -- Tuberculose: Tosse (muito comum)
	(1, 2, 'comum'), -- Tuberculose: Febre (comum)
	(1, 3, 'comum'), -- Tuberculose: Perda de peso (comum)
	
	(2, 2, 'muito comum'), -- Gripe: Febre (muito comum)
	(2, 4, 'comum'), -- Gripe: Dor de cabeça (comum)
	(2, 5, 'comum'), -- Gripe: Fadiga (comum)
	
	(3, 2, 'muito comum'), -- Malária: Febre (muito comum)
	(3, 6, 'muito comum'), -- Malária: Calafrios (muito comum)
	(3, 4, 'comum'), -- Malária: Dor de cabeça (comum)
	
	(4, 2, 'muito comum'), -- Dengue: Febre (muito comum)
	(4, 7, 'comum'), -- Dengue: Dor muscular (comum)
	(4, 8, 'comum'), -- Dengue: Erupção cutânea (comum)
	
	(5, 9, 'comum'), -- Hepatite B: Icterícia (comum)
	(5, 5, 'comum'), -- Hepatite B: Fadiga (comum)
	(5, 10, 'comum'), -- Hepatite B: Dor abdominal (comum)
	
	(6, 11, 'comum'), -- Sífilis: Úlceras (comum)
	(6, 8, 'comum'), -- Sífilis: Erupção cutânea (comum)
	(6, 2, 'pouco comum'), -- Sífilis: Febre (pouco comum)
	
	(7, 12, 'muito comum'), -- Candidíase: Coceira (muito comum)
	(7, 13, 'comum'), -- Candidíase: Corrimento (comum)
	(7, 14, 'pouco comum'), -- Candidíase: Dor ao urinar (pouco comum)
	
	(8, 8, 'muito comum'), -- Varicela: Erupção cutânea (muito comum)
	(8, 2, 'comum'), -- Varicela: Febre (comum)
	(8, 12, 'comum'), -- Varicela: Coceira (comum)
	
	(9, 2, 'muito comum'), -- Leptospirose: Febre (muito comum)
	(9, 7, 'comum'), -- Leptospirose: Dor muscular (comum)
	(9, 9, 'pouco comum'), -- Leptospirose: Icterícia (pouco comum)
	
	(10, 2, 'pouco comum'), -- Toxoplasmose: Febre (pouco comum)
	(10, 7, 'pouco comum'), -- Toxoplasmose: Dor muscular (pouco comum)
	(10, 30, 'pouco comum'), -- Toxoplasmose: Ínguas (pouco comum)
	
	(11, 2, 'muito comum'), -- Meningite: Febre (muito comum)
	(11, 4, 'muito comum'), -- Meningite: Dor de cabeça (muito comum)
	(11, 15, 'comum'), -- Meningite: Rigidez de nuca (comum)
	
	(12, 2, 'muito comum'), -- Febre Amarela: Febre (muito comum)
	(12, 9, 'comum'), -- Febre Amarela: Icterícia (comum)
	(12, 7, 'comum'), -- Febre Amarela: Dor muscular (comum)
	
	(13, 2, 'comum'), -- Zika: Febre (comum)
	(13, 8, 'comum'), -- Zika: Erupção cutânea (comum)
	(13, 16, 'comum'), -- Zika: Dor articular (comum)
	
	(14, 2, 'muito comum'), -- Chikungunya: Febre (muito comum)
	(14, 16, 'muito comum'), -- Chikungunya: Dor articular (muito comum)
	(14, 8, 'comum'), -- Chikungunya: Erupção cutânea (comum)
	
	(15, 8, 'muito comum'), -- Rubéola: Erupção cutânea (muito comum)
	(15, 2, 'comum'), -- Rubéola: Febre (comum)
	(15, 30, 'comum'), -- Rubéola: Ínguas (comum)
	
	(16, 8, 'muito comum'), -- Sarampo: Erupção cutânea (muito comum)
	(16, 2, 'muito comum'), -- Sarampo: Febre (muito comum)
	(16, 1, 'comum'), -- Sarampo: Tosse (comum)
	
	(17, 17, 'muito comum'), -- Tétano: Espasmos musculares (muito comum)
	(17, 31, 'muito comum'), -- Tétano: Rigidez (muito comum)
	(17, 2, 'pouco comum'), -- Tétano: Febre (pouco comum)
	
	(18, 18, 'muito comum'), -- Hanseníase: Manchas na pele (muito comum)
	(18, 19, 'comum'), -- Hanseníase: Perda de sensibilidade (comum)
	(18, 20, 'pouco comum'), -- Hanseníase: Fraqueza muscular (pouco comum)
	
	(19, 21, 'muito comum'), -- Cólera: Diarreia (muito comum)
	(19, 22, 'comum'), -- Cólera: Vômito (comum)
	(19, 23, 'comum'), -- Cólera: Desidratação (comum)
	
	(20, 2, 'muito comum'), -- Tifoide: Febre (muito comum)
	(20, 10, 'comum'), -- Tifoide: Dor abdominal (comum)
	(20, 8, 'pouco comum'), -- Tifoide: Erupção cutânea (pouco comum)
	
	(21, 24, 'muito comum'), -- Poliomielite: Paralisia (muito comum)
	(21, 2, 'comum'), -- Poliomielite: Febre (comum)
	(21, 7, 'comum'), -- Poliomielite: Dor muscular (comum)
	
	(22, 2, 'muito comum'), -- Raiva: Febre (muito comum)
	(22, 4, 'comum'), -- Raiva: Dor de cabeça (comum)
	(22, 17, 'comum'), -- Raiva: Espasmos musculares (comum)
	
	(23, 2, 'comum'), -- Esquistossomose: Febre (comum)
	(23, 10, 'comum'), -- Esquistossomose: Dor abdominal (comum)
	(23, 21, 'pouco comum'), -- Esquistossomose: Diarreia (pouco comum)
	
	(24, 21, 'muito comum'), -- Giardíase: Diarreia (muito comum)
	(24, 10, 'comum'), -- Giardíase: Dor abdominal (comum)
	(24, 29, 'comum'), -- Giardíase: Náusea (comum)
	
	(25, 21, 'muito comum'), -- Amebíase: Diarreia (muito comum)
	(25, 10, 'comum'), -- Amebíase: Dor abdominal (comum)
	(25, 2, 'pouco comum'), -- Amebíase: Febre (pouco comum)
	
	(26, 13, 'muito comum'), -- Tricomoníase: Corrimento (muito comum)
	(26, 12, 'comum'), -- Tricomoníase: Coceira (comum)
	(26, 14, 'pouco comum'), -- Tricomoníase: Dor ao urinar (pouco comum)
	
	(27, 2, 'comum'), -- Doença de Chagas: Febre (comum)
	(27, 25, 'comum'), -- Doença de Chagas: Inchaço no local da picada (comum)
	(27, 10, 'pouco comum'), -- Doença de Chagas: Dor abdominal (pouco comum)
	
	(28, 26, 'muito comum'), -- Leishmaniose: Feridas na pele (muito comum)
	(28, 2, 'comum'), -- Leishmaniose: Febre (comum)
	(28, 3, 'comum'), -- Leishmaniose: Perda de peso (comum)
	
	(29, 17, 'muito comum'), -- Tétano Neonatal: Espasmos musculares (muito comum)
	(29, 31, 'muito comum'), -- Tétano Neonatal: Rigidez (muito comum)
	(29, 2, 'pouco comum'), -- Tétano Neonatal: Febre (pouco comum)
	
	(30, 9, 'comum'), -- Hepatite A: Icterícia (comum)
	(30, 5, 'comum'), -- Hepatite A: Fadiga (comum)
	(30, 10, 'comum'), -- Hepatite A: Dor abdominal (comum)
	
	(31, 9, 'comum'), -- Hepatite C: Icterícia (comum)
	(31, 5, 'comum'), -- Hepatite C: Fadiga (comum)
	(31, 10, 'comum'), -- Hepatite C: Dor abdominal (comum)
	
	(32, 32, 'muito comum'), -- Herpes Simples: Feridas (muito comum)
	(32, 12, 'comum'), -- Herpes Simples: Coceira (comum)
	(32, 14, 'pouco comum'), -- Herpes Simples: Dor ao urinar (pouco comum)
	
	(33, 8, 'muito comum'), -- Varíola: Erupção cutânea (muito comum)
	(33, 2, 'muito comum'), -- Varíola: Febre (muito comum)
	(33, 7, 'comum'), -- Varíola: Dor muscular (comum)
	
	(34, 2, 'muito comum'), -- Mononucleose: Febre (muito comum)
	(34, 28, 'comum'), -- Mononucleose: Dor de garganta (comum)
	(34, 5, 'comum'), -- Mononucleose: Fadiga (comum)
	
	(35, 27, 'muito comum'), -- Caxumba: Inchaço das glândulas (muito comum)
	(35, 2, 'comum'), -- Caxumba: Febre (comum)
	(35, 4, 'comum'); -- Caxumba: Dor de cabeça (comum)