import React from "react";
import ReactDOM from "react-dom/client";
import "bootstrap/dist/css/bootstrap.min.css";
import "./index.css";
import reportWebVitals from "./reportWebVitals";

import candidados from "./candidados.json";
import PieChart from "./components/PieChart";
import Bars from "./components/Bars";

const root = ReactDOM.createRoot(document.getElementById("root"));

root.render(
  <React.StrictMode>
    <div className="container">
      {Object.keys(candidados).map((key) => {
        const cidade = candidados[key].cidade;
        const candidatosPrefeitura = candidados[key].candidatos_prefeitura.map(
          (candidato) => {
            return {
              nome: candidato.nome,
              totalDoacoesRecebido: candidato.total_doacoes_recebido,
              fotinho: candidato.fotinho,
              bensDeclados: candidato.total_de_bens_declarados,
            };
          }
        );
        const candidatosCamara = candidados[
          key
        ].candidatos_camara_vereadores.map((candidato) => {
          return {
            nome: candidato.nome,
            totalDoacoesRecebido: candidato.total_doacoes_recebido,
            fotinho: candidato.fotinho,
            bensDeclados: candidato.total_de_bens_declarados,
          };
        });

        const totalDoacoesRecebido = candidatosPrefeitura
          .reduce((acc, candidato) => acc + candidato.totalDoacoesRecebido, 0)
          .toLocaleString("pt-BR", { style: "currency", currency: "BRL" });

        const totalDoacoesRecebidoCamara = candidatosCamara
          .reduce((acc, candidato) => acc + candidato.totalDoacoesRecebido, 0)
          .toLocaleString("pt-BR", { style: "currency", currency: "BRL" });

        return (
          <div className="row my-4">
            <div className="col-md-6">
              <h3>Prefeitura de {cidade}</h3>
              <h3>Total recebido de doações: {totalDoacoesRecebido}</h3>
              <h4>Distribuição de receitas por candidato</h4>
              <PieChart
                data={{
                  labels: candidatosPrefeitura.map(
                    (candidato) => candidato.nome
                  ),
                  values: candidatosPrefeitura.map(
                    (candidato) => candidato.totalDoacoesRecebido
                  ),
                }}
              />
              <h4>Total recebido por candidato</h4>
              <ul className="list-group">
                {candidatosPrefeitura.map((candidato) => (
                  <li className="list-group-item">
                    <img
                      className="img-responsive rounded"
                      src={candidato.fotinho}
                      width={50}
                      height={60}
                    />
                    {candidato.nome}
                    {candidato.totalDoacoesRecebido.toLocaleString("pt-BR", {
                      style: "currency",
                      currency: "BRL",
                    })}
                  </li>
                ))}
              </ul>
              <Bars
                labels={candidatosPrefeitura.map((candidato) => candidato.nome)}
                values={candidatosPrefeitura.map((candidato) =>
                  parseFloat(candidato.bensDeclados)
                )}
              />
            </div>
            <div className="col-6">
              <h3 className="">Câmara municipal de {cidade}</h3>
              <h3>Total recebido de doações: {totalDoacoesRecebidoCamara}</h3>
              <h4>Distribuição de receitas por candidato</h4>
              <PieChart
                data={{
                  labels: candidatosCamara.map((candidato) => candidato.nome),
                  values: candidatosCamara.map(
                    (candidato) => candidato.totalDoacoesRecebido
                  ),
                }}
              />
              <h4>Total recebido por candidato</h4>
              <ul className="list-group">
                {candidatosCamara.map((candidato) => (
                  <li className="list-group-item">
                    <img
                      className="img-responsive rounded"
                      src={candidato.fotinho}
                      width={50}
                      height={60}
                    />
                    {candidato.nome}
                    {candidato.totalDoacoesRecebido.toLocaleString("pt-BR", {
                      style: "currency",
                      currency: "BRL",
                    })}
                  </li>
                ))}
              </ul>
              <Bars
                labels={candidatosCamara.map((candidato) => candidato.nome)}
                values={candidatosCamara.map((candidato) =>
                  parseFloat(candidato.bensDeclados)
                )}
              />
            </div>
          </div>
        );
      })}
    </div>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
