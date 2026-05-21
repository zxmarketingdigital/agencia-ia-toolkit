// Toolkit Agência IA — Workers Assets entry
// Quando configurado com [assets], o runtime serve estáticos automaticamente.
// Este worker existe apenas pra satisfazer o requisito de `main` no wrangler.toml.
export default {
  async fetch(request, env) {
    return env.ASSETS.fetch(request);
  }
};
