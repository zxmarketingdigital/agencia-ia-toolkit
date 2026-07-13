// toolkit.zxlab.com.br → CONSOLIDADO na área única (25/Jun/2026)
// O Toolkit virou a aba "Skills e Mini Apps" dentro da área de membros única.
// Redirect 301 permanente para a área consolidada.
export default {
  async fetch() {
    return Response.redirect("https://agencia-ia-automatizada.zxlab.com.br/", 301);
  }
};
