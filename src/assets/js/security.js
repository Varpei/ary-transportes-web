(function () {
  'use strict';

  var allowedUrls = [
    'https://wa.me/5563992935934',
    'https://wa.me/5563992930031',
    'https://www.instagram.com/_arytransporte/'
  ];

  function sanitizeText(input, maxLength) {
    var limit = typeof maxLength === 'number' ? maxLength : 120;
    if (typeof input !== 'string') {
      return '';
    }

    return input
      .replace(/[<>'"`;\\\/{}\[\]()]/g, '')
      .replace(/javascript:/gi, '')
      .replace(/data:/gi, '')
      .replace(/vbscript:/gi, '')
      .trim()
      .slice(0, limit);
  }

  function sanitizeUrl(url) {
    var value = typeof url === 'string' ? url.trim() : '';
    return allowedUrls.some(function (allowed) {
      return value.indexOf(allowed) === 0;
    }) ? value : '';
  }

  function validatePhone(phone) {
    return phone === '5563992935934' || phone === '5563992930031'
      ? phone
      : '5563992935934';
  }

  function buildWhatsAppUrl(phoneKey, payload) {
    var phone = phoneKey === 'secundario' ? '5563992930031' : '5563992935934';
    var data = payload || {};
    var fields = {
      nome: sanitizeText(data.nome || 'Cliente via Site', 60),
      servico: sanitizeText(data.servico || 'Fretamento / Viagem', 60),
      rota: sanitizeText(data.rota || 'Tocantins e Maranhão (TO / MA)', 100),
      data: sanitizeText(data.data || 'A combinar', 40),
      passageiros: sanitizeText(String(data.passageiros || 'Não informado'), 20),
      observacoes: sanitizeText(data.obs || data.observacoes || 'Nenhuma', 160)
    };
    var message = [
      '*Olá, ARY Transportes e Viagens!*',
      'Gostaria de solicitar um orçamento pelo site:',
      '',
      '*Nome:* ' + fields.nome,
      '*Modalidade:* ' + fields.servico,
      '*Origem/Destino ou Escola:* ' + fields.rota,
      '*Data/Período:* ' + fields.data,
      '*Passageiros:* ' + fields.passageiros,
      '*Observações:* ' + fields.observacoes
    ].join('\n');
    var baseUrl = sanitizeUrl('https://wa.me/' + validatePhone(phone));
    return baseUrl ? baseUrl + '?text=' + encodeURIComponent(message) : '';
  }

  window.ARYSecurity = Object.freeze({
    sanitizeText: sanitizeText,
    sanitizeUrl: sanitizeUrl,
    validatePhone: validatePhone,
    buildWhatsAppUrl: buildWhatsAppUrl,
    buildSafeWhatsAppUrl: function (phone, fields) {
      return buildWhatsAppUrl(
        phone === '5563992930031' ? 'secundario' : 'principal',
        fields
      );
    }
  });
})();
