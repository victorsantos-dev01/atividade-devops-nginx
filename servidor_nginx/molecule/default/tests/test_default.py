def test_nginx_instalado_e_rodando(host):
    # 1. Pacote instalado
    pacote_nginx = host.package("nginx")
    assert pacote_nginx.is_installed

    # 2. Serviço rodando e habilitado no boot
    servico_nginx = host.service("nginx")
    assert servico_nginx.is_running
    assert servico_nginx.is_enabled

    # 3. Porta 80 escutando
    porta_web = host.socket("tcp://0.0.0.0:80")
    assert porta_web.is_listening