/*
  --------------------------------------------------------------------------------------
  Função para obter a lista existente do servidor via requisição GET
  --------------------------------------------------------------------------------------
*/
const getList = async () => {
  let url = 'http://127.0.0.1:5000/idosos';
  fetch(url, {
    method: 'get',
  })
    .then((response) => response.json())
    .then((data) => {
      data.idosos.forEach(item => insertList(item.nome, item.cpf, item.idade, item.nomeResponsavel, item.numResponsavel))
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Chamada da função para carregamento inicial dos dados
  --------------------------------------------------------------------------------------
*/
getList()


/*
  --------------------------------------------------------------------------------------
  Função para colocar um item na lista do servidor via requisição POST
  --------------------------------------------------------------------------------------
*/
const postItem = async (inputIdoso, inputCpf, inputIdade, inputNomeResponsavel, inputNumResponsavel) => {
  const formData = new FormData();
  formData.append('nome', inputIdoso);
  formData.append('cpf', inputCpf);
  formData.append('idade', inputIdade);
  formData.append('nomeResponsavel', inputNomeResponsavel);
  formData.append('numResponsavel', inputNumResponsavel);

  let url = 'http://127.0.0.1:5000/idoso';
  fetch(url, {
    method: 'post',
    body: formData
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}


/*
  --------------------------------------------------------------------------------------
  Função para criar um botão close para cada item da lista
  --------------------------------------------------------------------------------------
*/
const insertButton = (parent) => {
  let span = document.createElement("span");
  let txt = document.createTextNode("\u00D7");
  span.className = "close";
  span.appendChild(txt);
  parent.appendChild(span);
}


/*
  --------------------------------------------------------------------------------------
  Função para remover um item da lista de acordo com o click no botão close
  --------------------------------------------------------------------------------------
*/
const removeElement = () => {
  let close = document.getElementsByClassName("close");
  // var table = document.getElementById('myTable');
  let i;
  for (i = 0; i < close.length; i++) {
    close[i].onclick = function () {
      let div = this.parentElement.parentElement;
      const nomeItem = div.getElementsByTagName('td')[0].innerHTML
      if (confirm("Você tem certeza?")) {
        div.remove()
        deleteItem(nomeItem)
        alert("Removido!")
      }
    }
  }
}

/*
  --------------------------------------------------------------------------------------
  Função para deletar um item da lista do servidor via requisição DELETE
  --------------------------------------------------------------------------------------
*/
const deleteItem = (item) => {
  console.log(item)
  let url = 'http://127.0.0.1:5000/idoso?nome=' + item;
  fetch(url, {
    method: 'delete'
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Função para adicionar um novo item com nome, cpf, iadde, nomeResponsavel e numResponsavel 
  --------------------------------------------------------------------------------------
*/
const newItem = () => {
  let inputIdoso = document.getElementById("nome").value;
  let inputCpf = document.getElementById("cpf").value;
  let inputIdade = document.getElementById("idade").value;
  let inputNomeResponsavel = document.getElementById("responsavel").value;
  let inputNumResponsavel = document.getElementById("celular").value;

  let formValid = true;

  // Validação do campo "Nome"
  if (!nome.checkValidity()) {
    nomeError.style.display = 'inline';
    formValid = false;
} else {
    nomeError.style.display = 'none';
}

// Validação do campo "CPF"
if (!cpf.checkValidity()) {
    cpfError.style.display = 'inline';
    formValid = false;
} else {
    cpfError.style.display = 'none';
}

// Validação do campo "Idade"
if (!idade.checkValidity()) {
  idadeError.style.display = 'inline';
  formValid = false;
} else {
  idadeError.style.display = 'none';
}

// Validação do campo "Responsável"
if (!responsavel.checkValidity()) {
  responsavelError.style.display = 'inline';
  formValid = false;
} else {
  responsavelError.style.display = 'none';
}

// Validação do campo "Fone Responsável"
if (!celular.checkValidity()) {
  celularError.style.display = 'inline';
  formValid = false;
} else {
  celularError.style.display = 'none';
}
// Se o formulário não for válido, impedir o envio
if (!formValid) {
  alert("Verifique os campos obrigatórios!");
   
} else {
  insertList(inputIdoso, inputCpf, inputIdade, inputNomeResponsavel, inputNumResponsavel)
  postItem(inputIdoso, inputCpf, inputIdade, inputNomeResponsavel, inputNumResponsavel)
  alert("Idoso adicionado!")
}






 /* if (inputIdoso === '') {
    alert("Escreva o nome de um idoso!");
  } else if ((inputCpf === '') || (inputIdade === '')) {
    alert("Os campos marcados são obrigatórias!");*/
    // Validação do campo "Nome"
    
  /*} else {*/
   /* insertList(inputIdoso, inputCpf, inputIdade, inputNomeResponsavel, inputNumResponsavel)
    postItem(inputIdoso, inputCpf, inputIdade, inputNomeResponsavel, inputNumResponsavel)
    alert("Idoso adicionado!")*/
  }
//}

/*
  --------------------------------------------------------------------------------------
  Função para inserir idosos na lista apresentada
  --------------------------------------------------------------------------------------
*/
const insertList = (nome, cpf, idade, responsavel, numero) => {
  var item = [nome, cpf, idade, responsavel, numero]
  var table = document.getElementById('myTable');
  var row = table.insertRow();

  for (var i = 0; i < item.length; i++) {
    var cel = row.insertCell(i);
    cel.textContent = item[i];
  }
  insertButton(row.insertCell(-1))
  document.getElementById("nome").value = "";
  document.getElementById("cpf").value = "";
  document.getElementById("idade").value = "";
  document.getElementById("responsavel").value = "";
  document.getElementById("celular").value = "";

  removeElement()
}

document.getElementById('form-group').addEventListener('submit', function(event) {
  // Impede o envio do formulário se houver campos inválidos
  let formValid = true;

  const nome = document.getElementById('nome');
  const email = document.getElementById('email');
  const nomeError = document.getElementById('nomeError');
  const emailError = document.getElementById('emailError');

  // Validação do campo "Nome"
  if (!nome.checkValidity()) {
      nomeError.style.display = 'inline';
      formValid = false;
  } else {
      nomeError.style.display = 'none';
  }

  // Validação do campo "E-mail"
  if (!email.checkValidity()) {
      emailError.style.display = 'inline';
      formValid = false;
  } else {
      emailError.style.display = 'none';
  }

  // Se o formulário não for válido, impedir o envio
  if (!formValid) {
      event.preventDefault();
  }
});