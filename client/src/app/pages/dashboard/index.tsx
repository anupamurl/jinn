import Form from 'react-bootstrap/Form'
import { useAppDispatch } from '../../redux/hooks'
import { resetState } from '../../redux/slices/auth.slice'
import * as xlsx from "xlsx";
import { socket } from '../../../socket';
import { useState } from 'react';
import { Field, Formik } from 'formik';
import { useSearchMutation    } from '../../services/articles.service'
import   People   from "./people"
const Dashboard = () => {
    const [isConnected, setIsConnected] = useState(socket.connected);
    const [fooEvents, setFooEvents] = useState([]);
    const [excle, setExcle] = useState({
        "Traditional":"",
        "Redirection" : "",
        "Profile" :""
    });
    const friendsArray = [
        {
            peoples : [ ]
        }
    ];

    const [peopleData, setPeopleData] = useState(friendsArray);
    const [transactional, setTransactional] = useState<any[]>([]);
    const [navigational, setNavigational] = useState<any[]>([]);

    const [search, { data, error, isLoading }] = useSearchMutation()
    const dispatch = useAppDispatch()
    const logout = () => {
        dispatch(resetState())
    }
    const handleAddFriend = (d: any) => {

        console.log(d)
        const newData = [...peopleData]    
        newData.splice(0,0,d);
        setPeopleData(newData);
        const peoplelist = d.peoples.concat([...transactional])
        setTransactional(peoplelist)
         
        
    };


    const handlePeople = (d:any) =>{    
        const arr: string[] = [];        
        arr.push(d)
        const peoplelist = arr.concat([...navigational])
        setNavigational(peoplelist)

    }
    const readUploadFile = (e:any) => {
        e.preventDefault();
        var Obj:any = {}
        if (e.target.files) {
            const reader = new FileReader();
            reader.onload = (e:any) => {
                const data = e.target.result;
                const workbook = xlsx.read(data, { type: "array" });
                const sheetName = workbook.SheetNames[0];
                const worksheet = workbook.Sheets[sheetName];
                const json = xlsx.utils.sheet_to_json(worksheet);
                console.log(json);
                json.forEach((node:any)=>{
                   if(!("Traditional" in Obj)){

                    Obj['Traditional'] = node['Traditional']
                    Obj['Redirection'] = node['Redirection']
                    Obj['Profile'] = node['Profile']

                   }
                   else{                     
                        if ( node['Traditional']  ){
                            Obj['Traditional'] = Obj['Traditional'] + "," +  node['Traditional']  
                        }
                        if (node['Redirection']  ){
                            Obj['Redirection'] = Obj['Redirection'] + "," +  node['Redirection']  
                        }
                        if (node['Profile'] ){
                            Obj['Profile'] = Obj['Profile'] + "," +  node['Profile']  
                        }                    
                    }


                })
                
                setExcle(Obj)
            };
            reader.readAsArrayBuffer(e.target.files[0]);
        }
    }

    socket.on('events', (data) => {

        if(Object.keys(data).indexOf("comment")<0){
            handleAddFriend(data)
        }
        else{

            handlePeople(data)
        }

    });


    const handleSearch = (formValue: { keyword: string; people: string, limit: number ,
linkedindata : boolean ,
facebook : boolean ,
google : boolean ,
btob : boolean 

        }) => {
        let { keyword, people, limit , linkedindata , facebook , google , btob } = formValue
        people = excle.Profile
        keyword = excle.Traditional 
        let postSearch = excle.Redirection      

       search({ keyword,people , postSearch , limit , linkedindata , facebook , google , btob })
    }

    return (
        <div className="main_text_div">
            <a href={void (0)} onClick={logout} className='logoutBtn' >logout</a>
            <div className="main_index_div">
                <div className="single_index_div first_div">
                    <div className="index_heading_div">
                        <h3 className="heading_color">Playground</h3>
                        <div className="position-relative upload_button">
                        <span className="input_upload_button"><img src="image/plus_icon.svg" alt="" height="10"
                                width="10" /></span>
                        <input type="file"  
                        
                         
                        name="upload"
                        id="upload"
                        onChange={readUploadFile}
                        
                        />
                    </div>
                    </div>

    <Formik
                                initialValues={{
                                    keyword: '',
                                    people: 'ceo',
                                    limit: 1,
                                    linkedindata : false,
                                    facebook : false,
                                    google : false,
                                    btob: false

                                }}
                                onSubmit={handleSearch}
                            >
                                {({ handleSubmit , setFieldValue   }) => (

                                    <Form noValidate onSubmit={handleSubmit}>
                    <div className="index_desc_div">
                    
                        <div>
                           
                                        <div className='form_input_div'>

                                     

                                         {   Object.entries(excle).map(function(key,val) {
    return  <div>
        <div className="mb-30">
    <h3 className="text-white pb-10 font-16">{ (key[1])? key[0] : ""}</h3>
    <p className="light_color_white"> {key[1]}
 
    </p>
</div></div>
}) }



                                             

                                        </div>

 


 
                                        
                                      

                        </div>


                                
                    </div>

                    <div className="fix_text_div">
                        <div className="light_color_white Custplay">
                            <ul className="custcheckmark">

                      
                                <li>
                                    
                                    
                                    <Field
   type="checkbox"
   name='linkedindata'
   id='linkedindata'
   label='Check the mark'
 
/> <label className="custcheck"> Linkedin  Data

                               

                             
                                    </label>
                                </li>


  <li>
                                    
                                    
                                    <Field
   type="checkbox"
   name='facebook'
   id='facebook'
   label='Check the mark'
 
/> <label className="custcheck">  Facebook 

                               

                             
                                    </label>
                                </li>



                                  <li>
                                    
                                    
                                    <Field
   type="checkbox"
   name='google'
   id='google'
   label='Check the mark'
 
/> <label className="custcheck">  Google 

                               

                             
                                    </label>
                                </li>


    <li>
                                    
                                    
                                    <Field
   type="checkbox"
   name='btob'
   id='btob'
   label='Check the mark'
 
/> <label className="custcheck">  B2B Review 

                               

                             
                                    </label>
                                </li>




             
           

                                  
                                
                               
                            </ul>

                            
                        </div>
                      

                            <button type="submit"  className="fix_footer_button text-center" ><img src="image/Play.svg" /></button>
                    </div>


                        </Form>

                                )}

                            </Formik>
                </div>
                <div className="single_index_div second_div">
                    <div className="index_heading_div">
                        <h3 className="heading_color">Buyer intent mining</h3>

                    </div>
                    <div className="index_desc_div">

                        {

                            peopleData.map((item: any) => {
                                return <div className="description mb-30 light_color_white limited-text">
                                    <p>{item.jobtitle}</p>
                                      <p>  {item.aboutjob}                             
 </p>
                                </div>
                            })

                        }



                    </div>
                </div>
                <div className="single_index_div thid_div">
                    <div className="index_heading_div">
                        <h3 className="heading_color">Transactional</h3>
                        <div className="position-relative">
                            <span className="ps-2 text-white digitdownload">{transactional.length}</span>
                            <span className="downloaddigi"><img src="image/download.svg" alt="" height="15"
                                width="15" /></span>
                        </div>
                    </div>
                    <div className="index_desc_div">
                     
                                {

                                            transactional.map((item:any, index:number) => {
                                                return <div className="mb-30">
                                                <h3 className="text-white pb-10 font-16">{item.name}</h3>
                                                <p className="light_color_white">
                                                    <div>{item.subtitle}  </div>
                                                   <div> Phone :  {item.phone} </div>
                                                    <div>  email :  {item.email} </div>
                                                    
                                                    
                                                 

                                                     </p>
                                                    
                                            </div>
                                  
                                                                                                })
                                

                        }

                        
                          
                     

                    </div>
                </div>
                <div className="single_index_div thid_div">
                    <div className="index_heading_div">
                        <h3 className="heading_color">Navigational</h3>
                        <div className="position-relative">
                            <span className="ps-2 text-white digitdownload">{navigational.length}</span>
                            <span className="downloaddigi"><img src="image/download.svg" alt="" height="15"
                                width="15" /></span>
                        </div>
                    </div>
                    <div className="index_desc_div">
                     
                                {

navigational.map((item:any, index:number) => {
                                                return <div className="mb-30">
                                                <h3 className="text-white pb-10 font-16">{item.name}</h3>
                                                <p className="light_color_white">
                                                    <div>{item.subtitle}  </div>
                                                   <div> Phone :  {item.phone} </div>
                                                    <div>  email :  {item.email} </div>
                                                    
                                                    
                                                

                                                     </p>
                                                    
                                            </div>
                                  
                                                                                                })
                                

                        }

                        
                          
                     

                    </div>
                </div>

                <div className="single_index_div fourth_div">
                    <div className="index_heading_div">
                        <h3 className="heading_color">Company Found</h3>
                        <div className="position-relative ">
                            <span className="ps-2 text-white digitdownload">{peopleData.length-1}</span>
                            <span className="downloaddigi"><img src="image/download.svg" alt="" height="15"
                                width="15" /></span>
                        </div>
                    </div>
                    <div className="index_desc_div">
                        
                   



                           {

                                            peopleData.map((item:any, index) => {
                                                return <div className="mb-30">
                   
                                      <h3 className="text-white pb-10 font-16">{item.cname}  </h3>
                            <p className="light_color_white">


                                { item.companyattr && item.companyattr.Attribute.map((item:any)=>{


return<div>{item}</div>


                                })}
                        </p>
                        </div>
                                  
                                                                                                })
                                

                        }


                        



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

