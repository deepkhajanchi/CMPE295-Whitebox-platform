import React, { Component } from "react";
import { Route } from 'react-router-dom';
import Login from '../src/components/Auth/login';
import Register from '../src/components/Auth/register';
import TestPage from '../src/components/Testpage/testpage';

class Main extends Component{
    render(){
        return(
            <div>
                <Route exact path="/"><Login/> </Route>
                <Route path="/login"><Login/> </Route>
                <Route path="/register"><Register/></Route>
                <Route path="/testpage"><TestPage/></Route>
            </div>
        )
    }
}
export default Main;