import React from 'react';
import FullCalendar from '@fullcalendar/react';
import esLocale from '@fullcalendar/core/locales/es';
import dayGridPlugin from '@fullcalendar/daygrid';
import timeGridPlugin from '@fullcalendar/timegrid';
import interactionPlugin from '@fullcalendar/interaction';
import rrulePlugin from '@fullcalendar/rrule';
import bootstrapPlugin from '@fullcalendar/bootstrap';
import Modal from './Modal';
import Navbar from './Navbar';
import './main.scss';


export default class DemoApp extends React.Component {

  calendarComponentRef = React.createRef()
  state = {
    calendarEvents: 'http://localhost:8000/events',
    isModalOpen: false
  }

  render() {
    return (
      <div className='app'>
        <div className='top'>
          <Navbar show="true" />
          <button className="btn btn-primary" onClick={this.toggleModal}>Open Modal</button>&nbsp;
        </div>
        <div className='calendar'>
          <FullCalendar
            defaultView="timeGridWeek"
            themeSystem="bootstrap"
            locale={esLocale}
            header={{
              left: 'prev,next today',
              center: 'title',
              right: 'dayGridMonth,timeGridWeek,timeGridDay,listWeek'
            }}
            plugins={[dayGridPlugin, timeGridPlugin, interactionPlugin, rrulePlugin, bootstrapPlugin]}
            ref={this.calendarComponentRef}
            events={this.state.calendarEvents}
            dateClick={this.handleDateClick}
          />
          <Modal show={this.state.isModalOpen}
            onClose={this.toggleModal}>
          </Modal>
        </div>
      </div>
    )
  }

  toggleModal = () => {
    this.setState({
      isModalOpen: !this.state.isModalOpen
    })
  }

  handleDateClick = (arg) => {
    this.toggleModal()
    this.props.start=arg.date
  }

}
