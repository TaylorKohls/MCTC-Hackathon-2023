import * as React from 'react';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';

export default function ImgMediaCard() {
  return (
    <>
    <Card sx={{ maxWidth: 800 }}>
      <CardMedia
        component="img"
        alt="US BANK HACKATHON 2023"
        height="440"
        image="\static\logo1.png"
      />
      <CardContent>
        <Typography gutterBottom variant="h5" component="div">
          Hackovation
        </Typography>
        <Typography variant="body2" color="text.secondary">
          GIZZARD
        </Typography>
      </CardContent>
      <CardActions>
        <Button size="small">HomePage</Button>
        <Button size="small">Sign Out</Button>
      </CardActions>
    </Card>
    <div>




    </div>
</>



     );
     
}