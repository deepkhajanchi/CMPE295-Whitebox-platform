import React,{ Component} from 'react';
import Navbar from '../Navbar/navbar';

class TestPage extends Component{
    render(){
        return(
            <div className="container">
            <div>
                <Navbar/>
            </div>
            <div className="row">
                This is test page
            </div>
            </div>
        )
    }
}
export default TestPage;