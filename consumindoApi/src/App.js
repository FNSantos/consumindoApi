import logo from './logo.svg';
import './App.css';
import React, { useState, useEffect } from 'react';

function App() {
    var [numberOfUsers, setNumberOfUsers] = useState(0)
    var [data, setData] = useState([]);

    const getData=()=>{
        fetch('http://127.0.0.1:5000/v1/consultar', {mode: 'no-cors'}
        )
        .then(function(response){
            console.log(response)
            
            setNumberOfUsers(response.length)
            // setData(response);
        })
      }

      return (
        <div className="CallApi">
            <div style={{backgroundColor:'black'}} className="display-board">
                <h4 style={{color: 'white'}}>Usuarios Criados</h4>
                <div className="number" style={{color: 'white'}}>
                    {numberOfUsers}
                </div>
                <div className="btn">
                    <button type="button" onClick={(e) => getData()} className="btn btn-warning">Buscar usuários</button>
                </div>
            </div>
        </div>
    );
}

export default App;
