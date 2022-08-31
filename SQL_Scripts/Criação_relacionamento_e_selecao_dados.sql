Use analise_risco;
start transaction;
DELETE FROM dados_mutuarios where person_id = '';
ALTER TABLE DADOS_MUTUARIOS ADD PRIMARY KEY (person_id);
ALTER TABLE HISTORICOS_BANCO ADD PRIMARY KEY (cb_id);
ALTER TABLE ID ADD CONSTRAINT FK_dados_mutuarios FOREIGN KEY (person_id) REFERENCES DADOS_MUTUARIOS(person_id);
ALTER TABLE ID ADD CONSTRAINT FK_historicos_banco FOREIGN KEY (cb_id) REFERENCES HISTORICOS_BANCO(cb_id);
commit;

SELECT person_age as Idade,
person_income as Salario_anual, 
person_home_ownership as Situacao_prop,
person_emp_length as Tempo_trabalho,
loan_intent as Motivo_emprest,
loan_grade as Pont_emprest,
loan_amnt as Total_emprest,
loan_int_rate as Tx_juros,
loan_status as Possib_inadimp,
loan_percent_income as Renda_pecentual,
cb_person_cred_hist_length as Periodo,
cb_person_default_on_file as Inadimplente
from dados_mutuarios d 
join id on d.person_id = id.person_id
join emprestimos e on e.loan_id = id.loan_id
join historicos_banco h on h.cb_id = id.cb_id;


