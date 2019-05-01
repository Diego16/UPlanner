import React from 'react';
//import PropTypes from 'prop-types';

class Navbar extends React.Component {
    render() {
        if (!this.props.show) {
            return null;
        }

        return (
            <nav className="navbar navbar-expand-lg navbar-dark bg-primary">
                <a className="navbar-brand" href="http://localhost:3000/">UPlanner</a>
                <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbar" aria-controls="navbar" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="navbar">
                    <ul className="navbar-nav mr-auto">
                        <li className="nav-item active">
                            <a className="nav-link" href="http://localhost:3000/">Calendario <span className="sr-only">(current)</span></a>
                        </li>
                        <li className="nav-item">
                            <a className="nav-link" href="http://localhost:3000/">Eventos universitarios</a>
                        </li>
                        <li className="nav-item">
                        {this.props.user.username}
                        </li>
                        <li className="nav-item">
                            <a className="nav-link my-2 my-sm-0" onClick={this.props.logout}>Cerrar sesión</a>
                        </li>
                    </ul>
                </div>
            </nav>
        )
    }
}
export default Navbar;