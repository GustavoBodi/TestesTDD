all:
	python -m unittest tests/EmpresaTest.py tests/FuncionarioTest.py tests/ProjetoTest.py tests/OcorrenciaTest.py

coverage:
	coverage run --source=src -m unittest tests/EmpresaTest.py tests/FuncionarioTest.py tests/ProjetoTest.py tests/OcorrenciaTest.py && coverage html
