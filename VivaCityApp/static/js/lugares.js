$(document).ready(function() {
    $('#calendario').fullCalendar({
        // Configuraciones y opciones del calendario
        header: {
            left: 'prev,next today',
            center: 'title',
            right: 'month,agendaWeek,agendaDay'
        },
        // Agrega eventos a tu calendario aquí (puedes obtenerlos dinámicamente desde tu servidor)
        events: [
            {
                title: 'Evento 1',
                start: '2024-01-20T10:00:00',
                end: '2024-01-20T12:00:00'
            },
            // Agrega más eventos según sea necesario
        ],
        // Configura el idioma a español
        locale: 'es'
    });
});