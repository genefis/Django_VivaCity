$(document).ready(function () {
    const events = mi_agenda.map(item => {
        return {
            title: item.nomEvento,
            start: item.fecha_inicio,
            end: item.fecha_fin
        }
    })
    console.log(events)

    $('#calendario').fullCalendar({
        aspectRatio: 2,
        updateSize: true,
        // Configuraciones y opciones del calendario
        header: {
            left: 'prev,next today',
            center: 'title',
            right: 'month,agendaWeek,agendaDay'
        },
        // Idioma
        locale: 'es',
        monthNames: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
        monthNamesShort: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'],
        dayNames: ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'],
        dayNamesShort: ['Dom', 'Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb'],
        // Agrega eventos a tu calendario aquí (puedes obtenerlos dinámicamente desde tu servidor)
        events // Se agregan del arreglo events
    });
});