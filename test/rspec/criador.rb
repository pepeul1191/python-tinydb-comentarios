# encoding: utf-8
require_relative 'app'
require 'json'

def crear
  RSpec.describe App do
    describe '1. Crear Comentarios a Criador: ' do
      it '1.1 Conexión con backend' do
        url = 'test/conexion'
        test = App.new(url)
        test.get()
        expect(test.response.code).to eq(200)
      end
      it '1.2 Crear Comentarios a Criador' do
        data = {
          :criador_id =>  1,
        }.to_json
        url = 'criador/crear?criador=' + data
        test = App.new(url)
        test.post()
        puts test.response.body
        expect(test.response.code).to eq(200)
        expect(test.response.body).not_to include('error')
        expect(test.response.body).to include('Se ha aperturado los comentarios al criador')
        expect(test.response.body).to include('success')
      end
    end
  end
end

def comentar
  RSpec.describe App do
    describe '2. Comentar el perfil de un criador: ' do
      it '2.1 Conexión con backend' do
        url = 'test/conexion'
        test = App.new(url)
        test.get()
        expect(test.response.code).to eq(200)
      end
      it '2.2 Comentar el perfil de un criador' do
        data = {
          :comentario_criador_id =>  1,
          :criador_id =>  1, # el que está haciendo el comentario
          :comentario => 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies'
        }.to_json
        url = 'criador/comentar?data=' + data
        test = App.new(url)
        test.post()
        puts test.response.body
        expect(test.response.code).to eq(200)
        expect(test.response.body).not_to include('error')
        expect(test.response.body).to include('Ha comentado el perfil del criador')
        expect(test.response.body).to include('success')
      end
    end
  end
end

def traer
  RSpec.describe App do
    describe '3. Traer los comentarios el perfil de un criador: ' do
      it '3.1 Conexión con backend' do
        url = 'test/conexion'
        test = App.new(url)
        test.get()
        expect(test.response.code).to eq(200)
      end
      it '3.2 Traer los comentarios el perfil de un criador' do
        data = 1.to_s
        url = 'criador/traer/' + data
        test = App.new(url)
        test.get()
        puts test.response.body
        expect(test.response.code).to eq(200)
        expect(test.response.body).not_to include('error')
        expect(test.response.body).to include('criador_id')
        expect(test.response.body).to include('comentarios')
      end
    end
  end
end

#crear
#comentar
traer