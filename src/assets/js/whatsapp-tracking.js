(function () {
  'use strict';
  window.dataLayer = window.dataLayer || [];
  window.ARYTracking = {
    pushEvent: function (eventName, metadata) {
      var details = metadata || {};
      var event = {
        event: eventName,
        timestamp: new Date().toISOString(),
        service_pillar: details.service_pillar || '',
        destination_phone: details.destination_phone || ''
      };
      window.dataLayer.push(event);
      return event;
    },
    trackConversion: function (eventName, metadata) {
      return this.pushEvent(eventName, metadata);
    }
  };

  document.addEventListener('DOMContentLoaded', function () {
    var form = document.getElementById('form-orcamento-ary');
    if (form) {
      form.addEventListener('submit', function (event) {
        event.preventDefault();
        var data = new FormData(form);
        var phoneKey = data.get('telefone') === '5563992930031' ? 'secundario' : 'principal';
        var safeUrl = window.ARYSecurity.buildWhatsAppUrl(phoneKey, {
          nome: data.get('nome'),
          servico: data.get('servico'),
          rota: data.get('rota'),
          data: data.get('data'),
          passageiros: data.get('passageiros'),
          observacoes: data.get('observacoes')
        });
        if (!safeUrl) return;
        window.ARYTracking.pushEvent('generate_lead', {
          service_pillar: data.get('servico'),
          destination_phone: data.get('telefone')
        });
        window.open(safeUrl, '_blank', 'noopener,noreferrer');
      });
    }

    document.querySelectorAll('[data-select-service], [data-ary-cta]').forEach(function (button) {
      button.addEventListener('click', function () {
        var service = button.getAttribute('data-select-service') || button.getAttribute('data-ary-cta');
        var select = document.getElementById('servico');
        if (select && service) select.value = service;
        var target = document.getElementById('orcamento');
        if (target) target.scrollIntoView({ behavior: 'smooth' });
        if (button.hasAttribute('data-direct-phone')) {
          var phone = button.getAttribute('data-direct-phone') === 'secundario'
            ? 'secundario' : 'principal';
          var url = window.ARYSecurity.buildWhatsAppUrl(phone, { servico: service });
          if (url) {
            window.ARYTracking.pushEvent('click_to_whatsapp', {
              service_pillar: service,
              destination_phone: phone
            });
            window.open(url, '_blank', 'noopener,noreferrer');
          }
        }
      });
    });
  });
})();
