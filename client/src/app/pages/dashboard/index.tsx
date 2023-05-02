import Form from 'react-bootstrap/Form'
import { useAppDispatch } from '../../redux/hooks'
import { resetState } from '../../redux/slices/auth.slice'


 

const Dashboard = () => {
 
 
    const dispatch = useAppDispatch()
 
    const logout = () => {
        dispatch(resetState())
      }
     

  return (
    
    <div className="main_text_div">
        <a href={void(0)} onClick={logout} >logout</a>
    <div className="main_index_div">
        <div className="single_index_div first_div">
            <div className="index_heading_div">
               
                    
                    <h3 className="heading_color">Playground</h3>
                <div className="position-relative upload_button">
                    <span className="input_upload_button"><img src="image/plus_icon.svg" alt="" height="10"
                            width="10" /></span>
                    <input type="file" name="myfile"/>
                </div>
                
            </div>
            <div className="index_desc_div">
               
                 

                <Form.Control as="textarea" className="custometexteditor"  rows={10}/>
                
            </div>
            <div className="fix_text_div">
                <div className="light_color_white Custplay">
                    <ul className="custcheckmark">
                         <li>
                            <label className="custcheck">Michelangelo
                               
                                <Form.Check  className="custometexteditor"   />
                                className="custometexteditor"
                                <span className="checkmark"></span>
                              </label>
                         </li>
                         <li>
                            <label className="custcheck">Rembrandt
                                <Form.Check  />
                                <span className="checkmark"></span>
                              </label>
                         </li>
                         <li>
                            <label className="custcheck">Claude Monet
                            <Form.Check  />
                                <span className="checkmark"></span>
                              </label>
                         </li>
                         <li>
                            <label className="custcheck">Salvador Dali
                            <Form.Check  />
                                <span className="checkmark"></span>
                              </label>
                         </li>
                         <li>
                            <label className="custcheck">Murano
                            <Form.Check  />
                                <span className="checkmark"></span>
                              </label>
                         </li>
                    </ul>
                    
                    <ul className="ninth_ul">
                        
                        <li>
                            <p className="light_color_white">Delete</p>
                            <p className="text-white">Status  <Form.Check  /> </p>
                        </li>
                    </ul>
                </div>
                <a href="" className="fix_footer_button text-center"><img src="image/Play.svg"/></a>
            </div>
        </div>
        <div className="single_index_div second_div">
            <div className="index_heading_div">
                <h3 className="heading_color">Buyer intent mining</h3>
                
            </div>
            <div className="index_desc_div">
                <div className="description mb-30 light_color_white ">
                    <p>Hello, I am looking for UX/ UI design agency or freelancer to... </p>
                </div>
                <div className="description mb-30 light_color_white ">
                    <p>Hello Connections.I am looking for UI/UX design agency for FTE. Agencies must be dealing with Figma.</p>
                </div>
                <div className="description mb-30 light_color_white ">
                    <p>Looking for a UX/UI Design Agency?Drop us a line. We’re ready to start something great together!https://www.usacd.com/ or hello@usacd.com</p>
                </div>
                <div className="description mb-30 light_color_white ">
                    <p>Hello, I am looking for UX/ UI design agency or freelancer to...</p>
                </div>
                <div className="description mb-30 light_color_white ">
                    <p>Hello Connections.I am looking for UI/UX design agency for FTE. Agencies must be dealing with Figma.</p>
                </div>
                <div className="description mb-30 light_color_white ">
                    <p>Looking for a UX/UI Design Agency?Drop us a line. We’re ready to start something great together!https://www.usacd.com/ or hello@usacd.com</p>
                </div>
                <div className="description mb-30 light_color_white ">
                    <p>Looking for a UX/UI Design Agency?Drop us a line. We’re ready to start something great together!https://www.usacd.com/ or hello@usacd.com</p>
                </div>
                <div className="description mb-30 light_color_white ">
                    <p>Hello, I am looking for UX/ UI design agency or freelancer to...</p>
                </div>
                <div className="">
                    <h3 className="text-white pb-10 font-16">Principal, Information Security</h3>
                    <p className="light_color_white">BYN MellonPittsburgh,  
                        Pennsylvania, United States 
                        31/03/2023</p>
                </div>
                
            </div>
        </div>
        <div className="single_index_div thid_div">
            <div className="index_heading_div">
                <h3 className="heading_color">Transactional</h3>
                <div className="position-relative">
                    <span className="ps-2 text-white digitdownload">3452</span>
                    <span className="downloaddigi"><img src="image/download.svg" alt="" height="15"
                            width="15" /></span>
                </div>
            </div>
            <div className="index_desc_div">
                <div className="mb-30">
                    <h3 className="text-white pb-10 font-16">Om Chaturvedi</h3>
                    <p className="light_color_white">Cyber Security Evangelist at Druva ,  
                        New Delhi 
                        Phone +91 83838 29223 
                        email inaif@gmail.com</p>
                </div>
                 
            </div>
        </div>
        <div className="single_index_div fourth_div">
            <div className="index_heading_div">
                <h3 className="heading_color">Navigational</h3>
                <div className="position-relative ">
                    <span className="ps-2 text-white digitdownload">3452</span>
                    <span className="downloaddigi"><img src="image/download.svg" alt="" height="15"
                            width="15" /></span>
                </div>
            </div>
            <div className="index_desc_div">
                <div className="mb-30">
                    <h3 className="text-white pb-10 font-16">Om Chaturvedi</h3>
                    <p className="light_color_white">Cyber Security Evangelist at Druva New Delhi  Phone <a
                            href="" className="remove_line">+91 83838 29223</a>  email
                        <a href="" className="remove_line">inaif@gmail.com</a>
                    </p>
                </div>
                <div className="mb-30">
                    <h3 className="text-white pb-10 font-16">Vishal Yadav</h3>
                    <p className="light_color_white">Cyber Security Evangelist at Druva  New Delhi  Phone <a
                            href="" className="remove_line">+91 83838 29223</a>   email
                        <a href="" className="remove_line">inaif@gmail.com</a>
                    </p>
                </div>
                <div className="mb-30">
                    <h3 className="text-white pb-10 font-16">Om Chaturvedi</h3>
                    <p className="light_color_white">Cyber Security Evangelist at Druva  New Delhi  Phone <a
                            href="" className="remove_line">+91 83838 29223</a>   email
                        <a href="" className="remove_line">inaif@gmail.com</a>
                    </p>
                </div>
                <div className="mb-30">
                    <h3 className="text-white pb-10 font-16">Vishal Yadav</h3>
                    <p className="light_color_white">Cyber Security Evangelist at Druva  New Delhi  Phone <a
                            href="" className="remove_line">+91 83838 29223</a>   email
                        <a href="" className="remove_line">inaif@gmail.com</a>
                    </p>
                </div>
            </div>
            
        </div>
        <div className="single_index_div fifth_div">
            <div className="index_heading_div">
                <h3 className="heading_color">Informational</h3>
                <div className="position-relative ">
                    <span className="ps-2 text-white digitdownload">3452</span>
                    <span className="downloaddigi"><img src="image/download.svg" alt="" height="15"
                            width="15" /></span>
                </div>
            </div>
            <div className="index_desc_div">
                <div className="mb-30">
                    <h3 className="text-white pb-10 font-16">Om Chaturvedi</h3>
                    <p className="light_color_white">Cyber Security Evangelist at Druva  New Delhi  Phone <a
                            href="" className="remove_line">+91 83838 29223</a>   email
                        <a href="" className="remove_line">inaif@gmail.com</a>
                    </p>
                </div>
                <div className="mb-30">
                    <h3 className="text-white pb-10 font-16">Vishal Yadav</h3>
                    <p className="light_color_white">Cyber Security Evangelist at Druva  New Delhi  Phone <a
                            href="" className="remove_line">+91 83838 29223</a>   email
                        <a href="" className="remove_line">inaif@gmail.com</a>
                    </p>
                </div>
                <div className="mb-30">
                    <h3 className="text-white pb-10 font-16">Om Chaturvedi</h3>
                    <p className="light_color_white">Cyber Security Evangelist at Druva  New Delhi  Phone <a
                            href="" className="remove_line">+91 83838 29223</a>   email
                        <a href="" className="remove_line">inaif@gmail.com</a>
                    </p>
                </div>
                <div className="mb-30">
                    <h3 className="text-white pb-10 font-16">Vishal Yadav</h3>
                    <p className="light_color_white">Cyber Security Evangelist at Druva  New Delhi  Phone <a
                            href="" className="remove_line">+91 83838 29223</a>   email
                        <a href="" className="remove_line">inaif@gmail.com</a>
                    </p>
                </div>
            </div>
        </div>
        <div className="single_index_div sixth_div">
            <div className="index_heading_div">
                <h3 className="heading_color">Company Founded</h3>
                <div className="position-relative ">
                    <span className="ps-2 text-white digitdownload">3452</span>
                    <span className="downloaddigi"><img src="image/download.svg" alt="" height="15"
                            width="15" /></span>
                </div>
            </div>
            <div className="index_desc_div">
                <div className="mb-30">
                    <h3 className="text-white pb-10 font-16">Company name </h3>
                    <p className="light_color_white">Industry  No of People  Location   Website    Phone   Email
                    </p>
                </div>
                
                <div className="mb-30">
                    <h3 className="text-white pb-10 font-16">Company name </h3>
                    <p className="light_color_white">Industry  No of People  Location   Website    Phone   Email
                    </p>
                </div>
                <div className="mb-30">
                    <h3 className="text-white pb-10 font-16">Company name </h3>
                    <p className="light_color_white">Industry  No of People  Location   Website    Phone   Email
                    </p>
                </div>
                <div className="mb-30">
                    <h3 className="text-white pb-10 font-16">Company name </h3>
                    <p className="light_color_white">Industry  No of People  Location   Website    Phone   Email
                    </p>
                </div>
            </div>
        </div>
        <div className="single_index_div seventh_div">
            <div className="index_heading_div">
                <h3 className="heading_color">History</h3>
                
            </div>
            <div className="index_desc_div custcsssevandiv">
                <div className="">
                    <p className="light_color_white">What you want to do today
                    </p>
                    <h3 className="text-white pb-10 font-16">23745 Buyer Founded </h3>
                    
                </div>
                <div className="">
                    <p className="light_color_white">What you want to do today
                    </p>
                    <h3 className="text-white pb-10 font-16">23745 Buyer Founded </h3>
                    
                </div>
                <div className="">
                    <p className="light_color_white">What you want to do today
                    </p>
                    <h3 className="text-white pb-10 font-16">23745 Buyer Founded </h3>
                    
                </div>
                <div className="">
                    <p className="light_color_white">What you want to do today
                    </p>
                    <h3 className="text-white pb-10 font-16">23745 Buyer Founded </h3>
                    
                </div>

            </div>
        </div>
        
    </div>
</div>

    
  )
}

export default Dashboard
function dispatch(arg0: any) {
    throw new Error('Function not implemented.')
}

