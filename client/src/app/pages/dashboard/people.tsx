import React, { Component } from 'react';

interface TitleProps {
  title: string;
  subtitle?: string;
}

class People extends Component<any> {
  render() {
    const { ceo } = this.props;
    return (
      <>
         { ceo && ceo.map((item:any)=>{

          return   <div className="mb-30">
                        <h3 className="text-white pb-10 font-16">{item.name}</h3>
                        <p className="light_color_white">
                            <div>{item.subtitle}  </div>
                           <div> Phone :  {item.phone} </div>
                            <div>  email :  {item.email} </div> </p>
                    </div>

         })  }
       
      </>
    );
  }
}

export default People;