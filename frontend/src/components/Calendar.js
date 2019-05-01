import React, { Component } from 'react';
import { connect } from 'react-redux';
import FullCalendar from '@fullcalendar/react';
import esLocale from '@fullcalendar/core/locales/es';
import dayGridPlugin from '@fullcalendar/daygrid';
import timeGridPlugin from '@fullcalendar/timegrid';
import interactionPlugin from '@fullcalendar/interaction';
import rrulePlugin from '@fullcalendar/rrule';
import bootstrapPlugin from '@fullcalendar/bootstrap';
import Modal from './Modal';
import Navbar from './Navbar';
import { events, auth } from "../actions";


class Calendar extends Component {

  componentDidMount() {
    this.props.fetchEvents();
  }

  calendarComponentRef = React.createRef()
  state = {
    updateEventId: null,
    isModalOpen: false,
    start: new Date()
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
            events={this.state.events}
            dateClick={this.handleDateClick}
          />
          <Modal show={this.state.isModalOpen}
            onClose={this.toggleModal} start={this.state.start}>
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

  toggleStart = (date) => {
    this.setState({
      start: date
    })
  }

  handleDateClick = (arg) => {
    this.toggleStart(arg.date)
    this.toggleModal()
  }

}
const mapStateToProps = state => {
  return {
    events: state.events,
    user: state.auth.user,
  }
}

const mapDispatchToProps = dispatch => {
  return {
    fetchEvents: () => {
      dispatch(events.fetchEvents());
    },
    addEvent: (text) => {
      return dispatch(events.addEvent(text));
    },
    updateEvent: (id, text) => {
      return dispatch(events.updateEvent(id, text));
    },
    deleteEvent: (id) => {
      dispatch(events.deleteEvent(id));
    },
    logout: () => dispatch(auth.logout()),
  }
}


export default connect(mapStateToProps, mapDispatchToProps)(Calendar);
