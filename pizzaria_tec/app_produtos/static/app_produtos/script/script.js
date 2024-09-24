function onClickAddCart(id, nome_produto) {
    fetch('api/carrinho/adicionar/' + id)
        .then(response => {
            if (response.ok) {
                alert('Item ' + nome_produto + ' adicionado ao carrinho');
            } else {
                throw new Error('Request failed');
            }
        })
        .catch(error => {
            console.error('Erro:', error);
            alert('Erro ao adicionar o item ' + nome_produto + ' ao carrinho. Tente novamente.');
        });
}
